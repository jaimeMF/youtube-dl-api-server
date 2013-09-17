import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))

from youtube_dl_server import app

def main():
    app.run()

if __name__=='__main__':
    main()
