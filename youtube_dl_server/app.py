import webapp2

from .APIresponder import Api

app = webapp2.WSGIApplication([('/api/', Api)],
                              debug=True)
