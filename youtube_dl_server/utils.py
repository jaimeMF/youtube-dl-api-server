from youtube_dl.utils import YoutubeDLHandler, compat_urllib_request

def setup_url_handlers():
    opener = compat_urllib_request.build_opener( YoutubeDLHandler())
    opener.addheaders =[]
    compat_urllib_request.install_opener(opener)

def setup():
    setup_url_handlers()
