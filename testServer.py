from paste import httpserver

from app import app

"""
    A server for testing the api
"""

def main():
    httpserver.serve(app, host='localhost', port='9191')

if __name__ == '__main__':
    main()
