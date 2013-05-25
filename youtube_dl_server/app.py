import webapp2

from .API import url_map

app = webapp2.WSGIApplication(url_map,
                              debug=True)
