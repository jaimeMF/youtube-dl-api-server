import webapp2
import json

import youtube_dl

class NoneFile(object):
    '''
    A file-like object that does nothing
    '''
    def write(self,*args,**kaargs):
        pass
    def flush(self,*args,**kaargs):
        pass

class SimpleFileDownloader(youtube_dl.FileDownloader):
    def __init__(self,*args,**kargs):
        super(SimpleFileDownloader,self).__init__(*args,**kargs)
        self._screen_file=NoneFile()
    pass

def videos(url):
    '''
    Get a list with a dict for every video founded
    '''
    ies = youtube_dl.gen_extractors()[:-1] #We ignore GenericIE
    fd = SimpleFileDownloader({'outtmpl':'%(title)s'})
    for ie in ies:
        ie.set_downloader(fd)
        if ie.suitable(url):
            vids = ie.extract(url)
            return vids,ie

class Api(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'application/json'
        #Allow javascript get requests from other domains
        self.response.headers['Access-Control-Allow-Origin'] = '*'
        url = self.request.get("url")
        vids,ie = videos(url)
        dic = {'youtube-dl.version':youtube_dl.__version__,
               'url':url,
               'ie':ie.IE_NAME,
               'videos':vids}
        json_string = json.dumps(dic)
        self.response.out.write(json_string)
        

app = webapp2.WSGIApplication([('/api/', Api)],
                              debug=True)

def main():
    app.run()

if __name__=='__main__':
    main()
