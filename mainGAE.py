import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))

# Monkeypatch some youtube_dl functions that use features not available in GAE
import youtube_dl
# Modifying youtube_dl.utils.get_cachedir doesn't work
youtube_dl.extractor.youtube.get_cachedir = lambda *args, **kargs: None


from youtube_dl_server import app, setup

def main():
    setup()
    app.run()

if __name__=='__main__':
    main()
