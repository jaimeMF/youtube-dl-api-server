import argparse

from .app import app
from .version import __version__

"""
    A server for providing the app anywhere, no need for GAE
"""


def main():
    desc = """
           The youtube-dl API server.
           """

    parser = argparse.ArgumentParser(description=desc)

    parser.add_argument(
        '-p', '--port',
        default=9191,
        type=int,
        help='The port the server will use. The default is: %(default)s',
    )

    parser.add_argument(
        '--host',
        default='localhost',
        type=str,
        help='The host the server will use. The default is: %(default)s',
    )

    parser.add_argument(
        '--number-processes',
        default=5,
        type=int,
        help=('The number of processes the server will use. The default is: '
              '%(default)s'),
    )

    parser.add_argument('--version', action='store_true',
                        help='Print the version of the server')
    parser.add_argument('--ydl-proxy', type=str, help='''Use the specified HTTP/HTTPS/SOCKS proxy for youtube-dl. To enable SOCKS proxy, specify a proper scheme. For
                                     example socks5://127.0.0.1:1080/. Pass in an empty string (--proxy "") for direct connection''')
    args = parser.parse_args()
    if args.version:
        print(__version__)
        exit(0)
    app.ydl_proxy = args.ydl_proxy
    app.run(args.host, args.port, processes=args.number_processes)
