import logging
import traceback
import sys

import youtube_dl

from APIHandler import APIHandler


class NoneFile(object):
    '''
    A file-like object that does nothing
    '''
    def write(self, msg):
        pass

    def flush(self, *args, **kaargs):
        pass

    def isatty(self):
        return False


class ScreenFile(NoneFile):
    def write(self, msg):
        logging.debug(msg)


if not hasattr(sys.stderr, 'isatty'):
    #In GAE it's not defined and we must monkeypatch
    sys.stderr.isatty = lambda: False


class SimpleYDL(youtube_dl.YoutubeDL):
    def __init__(self, *args, **kargs):
        super(SimpleYDL, self).__init__(*args, **kargs)
        self._screen_file = ScreenFile()
        self.add_default_info_extractors()


def videos(url):
    '''
    Get a list with a dict for every video founded
    '''
    ydl_params = {
        'cachedir': None,
    }
    ydl = SimpleYDL(ydl_params)
    res = ydl.extract_info(url, download=False)

    #Do not return yet playlists
    def clean_res(result):
        r_type = result.get('_type', 'video')
        if r_type == 'video':
            videos = [result]
        elif r_type == 'playlist':
            videos = []
            for entry in result['entries']:
                videos.extend(clean_res(entry))
        elif r_type == 'compat_list':
            videos = []
            for r in result['entries']:
                videos.extend(clean_res(r))
        return videos
    return clean_res(res)


class Api(APIHandler):
    def get_response(self):
        errors = (youtube_dl.utils.DownloadError, youtube_dl.utils.ExtractorError)
        try:
            url = self.request.get("url")
            vids = videos(url)
            dic = {'youtube-dl.version': youtube_dl.__version__,
                   'url': url,
                   'videos': vids}
        except errors as err:
            dic = {'error': str(err)}
            logging.error(traceback.format_exc())
        return dic
