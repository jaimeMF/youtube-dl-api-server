from paste import httpserver

from app import app

"""
    A server for providing the app anywhere, no need for GAE
"""

def main():
    httpserver.serve(app, host='localhost', port='9191')

if __name__ == '__main__':
    main()
