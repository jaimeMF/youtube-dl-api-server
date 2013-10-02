from paste import httpserver
import argparse

from .app import app
from .version import __version__

from youtube_dl.utils import YoutubeDLHandler, compat_urllib_request

"""
    A server for providing the app anywhere, no need for GAE
"""


def setup_url_handlers():
    opener = compat_urllib_request.build_opener( YoutubeDLHandler())
    opener.addheaders =[]
    compat_urllib_request.install_opener(opener)

def setup():
    setup_url_handlers()

def main():
    desc = """
           The youtube-dl API server.
           """

    parser = argparse.ArgumentParser(description=desc)

    default_port = 9191
    port_help = 'The port the server will use. The default is: {}'
    port_help = port_help.format(default_port)
    parser.add_argument('-p', '--port',
                        default=default_port,
                        type=int,
                        help=port_help
                        )

    parser.add_argument('--version', action='store_true',
                        help='Print the version of the server')

    args = parser.parse_args()
    if args.version:
        print(__version__)
        exit(0)
    
    setup()
    httpserver.serve(app, host='localhost', port=args.port)

if __name__ == '__main__':
    main()
