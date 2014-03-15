#!/usr/bin/env python

import sys
# Allow direct execution
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
import json

from youtube_dl.utils import compat_urllib_parse
from youtube_dl_server.app import app


class ServerTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def get_json(self, *args, **kargs):
        resp = self.app.get(*args, **kargs)
        return json.loads(resp.data.decode(resp.charset))

    def get_video_info(self, url):
        return self.get_json('/api/?%s' % compat_urllib_parse.urlencode({'url': url}))

    def test_TED(self):
        """Test video (TED talk)"""
        test_url = "http://www.ted.com/talks/dan_dennett_on_our_consciousness.html"
        info = self.get_video_info(test_url)
        self.assertEqual(info["url"], test_url)

    def test_Vimeo(self):
        """Test Vimeo support"""
        test_url = 'http://vimeo.com/56015672'
        info = self.get_video_info(test_url)
        self.assertEqual(info["url"], test_url)

    def test_errors(self):
        resp = self.app.get('/api/?%s' % compat_urllib_parse.urlencode({'url': 'http://www.google.com'}))
        self.assertEqual(resp.status_code, 500)
        info = json.loads(resp.data.decode(resp.charset))
        self.assertIn('error', info)

    def test_extractors(self):
        resp = self.get_json('/api/extractors')
        ies = resp['extractors']
        self.assertIn('youtube', (ie['name'] for ie in ies))

if __name__ == '__main__':
    unittest.main()
