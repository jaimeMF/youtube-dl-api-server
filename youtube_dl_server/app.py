import functools
import logging
import traceback
import sys

from flask import Flask, jsonify, request
import youtube_dl
from youtube_dl.version import __version__ as youtube_dl_version
from .version import __version__ as youtube_dl_api_server_version


if not hasattr(sys.stderr, 'isatty'):
    # In GAE it's not defined and we must monkeypatch
    sys.stderr.isatty = lambda: False


class SimpleYDL(youtube_dl.YoutubeDL):
    def __init__(self, *args, **kargs):
        super(SimpleYDL, self).__init__(*args, **kargs)
        self.add_default_info_extractors()


def get_videos(url, extra_params):
    '''
    Get a list with a dict for every video founded
    '''
    ydl_params = {
        'format': 'best',
        'cachedir': False,
        'logger': app.logger.getChild('youtube-dl'),
    }
    ydl_params.update(extra_params)
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


@app.errorhandler(youtube_dl.utils.DownloadError)
@app.errorhandler(youtube_dl.utils.ExtractorError)
def handle_youtube_dl_error(error):
    logging.error(traceback.format_exc())
    result = jsonify({'error': str(error)})
    result.status_code = 500
    return result


class WrongParameterTypeError(ValueError):
    def __init__(self, value, type, parameter):
        message = '"{}" expects a {}, got "{}"'.format(parameter, type, value)
        super(WrongParameterTypeError, self).__init__(message)


@app.errorhandler(WrongParameterTypeError)
def handle_wrong_parameter(error):
    logging.error(traceback.format_exc())
    result = jsonify({'error': str(error)})
    result.status_code = 400
    return result


def query_bool(value, name, default=None):
    if value is None:
        return default
    value = value.lower()
    if value == 'true':
        return True
    elif value == 'false':
        return False
    else:
        raise WrongParameterTypeError(value, 'bool', name)


ALLOWED_EXTRA_PARAMS = {
    'playliststart': int,
    'playlistend': int,
    'playlist_items': str,
    'playlistreverse': bool,
    'matchtitle': str,
    'rejecttitle': str,
    'writesubtitles': bool,
    'writeautomaticsub': bool,
    'allsubtitles': bool,
    'subtitlesformat': str,
    'subtitleslangs': list,
}


@route_api('info')
@set_access_control
def info():
    url = request.args['url']
    extra_params = {}
    for k, v in request.args.items():
        if k in ALLOWED_EXTRA_PARAMS:
            convertf = ALLOWED_EXTRA_PARAMS[k]
            if convertf == bool:
                convertf = lambda x: query_bool(x, k)
            elif convertf == list:
                convertf = lambda x: x.split(',')
            extra_params[k] = convertf(v)
    result = get_videos(url, extra_params)
    key = 'info'
    if query_bool(request.args.get('flatten'), 'flatten', False):
        result = flatten_result(result)
        key = 'videos'
    result = {
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


@route_api('version')
@set_access_control
def version():
    result = {
        'youtube-dl': youtube_dl_version,
        'youtube-dl-api-server': youtube_dl_api_server_version,
    }
    return jsonify(result)
