from paste import httpserver
import argparse

from app import app

"""
    A server for providing the app anywhere, no need for GAE
"""

def main():

    desc="""
         The youtube-dl API server.
         """
    default_port = 9191
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('-p','--port',
                       default= default_port,
                       type=int,
                       help='The port the server will use. The default is: {}'.format(default_port)
                       )
    
    args = parser.parse_args()
    httpserver.serve(app, host='localhost', port=args.port)

if __name__ == '__main__':
    main()
