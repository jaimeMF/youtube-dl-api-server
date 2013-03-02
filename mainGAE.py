import webapp2

from APIresponder import Api

app = webapp2.WSGIApplication([('/api/', Api)],
                              debug=True)

def main():
    app.run()

if __name__=='__main__':
    main()
