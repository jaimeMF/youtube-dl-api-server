import functools
import logging
import traceback
import sys

from flask import Flask, jsonify, request, redirect
import youtube_dl

from youtube_dl.utils import compat_urllib_parse
from youtube_dl.version import __version__ as youtube_dl_version


if not hasattr(sys.stderr, 'isatty'):
    # In GAE it's not defined and we must monkeypatch
    sys.stderr.isatty = lambda: False


class SimpleYDL(youtube_dl.YoutubeDL):
    def __init__(self, *args, **kargs):
        super(SimpleYDL, self).__init__(*args, **kargs)
        self.add_default_info_extractors()


def get_videos(url):
    '''
    Get a list with a dict for every video founded
    '''
    ydl_params = {
        'format': 'best',
        'cachedir': False,
        'logger': app.logger.getChild('youtube-dl'),
    }
    ydl = SimpleYDL(ydl_params)
    res = ydl.extract_info(url, download=False)
    return res


def flatten_result(result):
    r_type = result.get('_type', 'video')
    if r_type == 'video':
        videos = [result]
    elif r_type == 'playlist':
        videos = []
        for entry in result['entries']:
            videos.extend(flatten_result(entry))
    elif r_type == 'compat_list':
        videos = []
        for r in result['entries']:
            videos.extend(flatten_result(r))
    return videos


app = Flask(__name__)


def route_api(subpath, *args, **kargs):
    return app.route('/api/' + subpath, *args, **kargs)


def set_access_control(f):
    @functools.wraps(f)
    def wrapper(*args, **kargs):
        response = f(*args, **kargs)
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response
    return wrapper


@route_api('')
@set_access_control
def api():
    response = redirect('/api/info?%s' % compat_urllib_parse.urlencode(request.args), 301)
    response.headers['Deprecated'] = 'Use "/api/info" instead'
    return response


@route_api('info')
@set_access_control
def info():
    url = request.args['url']
    errors = (youtube_dl.utils.DownloadError, youtube_dl.utils.ExtractorError)
    try:
        result = get_videos(url)
    except errors as err:
        logging.error(traceback.format_exc())
        result = jsonify({'error': str(err)})
        result.status_code = 500
        return result
    key = 'info'
    # Turn it on by default to keep backwards compatibility.
    if request.args.get('flatten', 'True').lower() == 'true':
        result = flatten_result(result)
        key = 'videos'
    result = {
        'youtube-dl.version': youtube_dl_version,
        'url': url,
        key: result,
    }
    return jsonify(result)


@route_api('extractors')
@set_access_control
def list_extractors():
    ie_list = [{
        'name': ie.IE_NAME,
        'working': ie.working(),
    } for ie in youtube_dl.gen_extractors()]
    return jsonify(extractors=ie_list)
