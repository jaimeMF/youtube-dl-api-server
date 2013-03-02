import webapp2
from paste import httpserver

from APIresponder import Api

"""
    A server for testing the api
"""

app = webapp2.WSGIApplication([('/api/', Api)],
                              debug=True)

def main():
    httpserver.serve(app, host='localhost', port='9191')

if __name__ == '__main__':
    main()
