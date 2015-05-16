#!/usr/bin/env python
from __future__ import unicode_literals

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

    def get_video_info(self, url, **kwargs):
        args = dict(url=url, **kwargs)
        return self.get_json('/api/info?%s' % compat_urllib_parse.urlencode(args))

    def test_TED(self):
        """Test video (TED talk)"""
        test_url = "http://www.ted.com/talks/dan_dennett_on_our_consciousness.html"
        info = self.get_video_info(test_url, flatten=False)
        self.assertEqual(info["url"], test_url)
        video_info = info['info']
        keys = ['url', 'ext', 'title']
        for k in keys:
            self.assertIn(k, video_info)
            self.assertIsNotNone(video_info[k])

    def test_Vimeo(self):
        """Test Vimeo support"""
        test_url = 'http://vimeo.com/56015672'
        info = self.get_video_info(test_url)
        self.assertEqual(info["url"], test_url)

    def test_extra_params(self):
        """Test extra parameters for YoutubeDL"""
        test_url = 'https://www.youtube.com/playlist?list=PLwiyx1dc3P2JR9N8gQaQN_BCvlSlap7re'
        info = self.get_video_info(test_url, playliststart='2', playlistend='2')
        ids = set(v['id'] for v in info['videos'])
        self.assertEqual(ids, {'FXxLjLQi3Fg'})

        test_url = 'https://www.youtube.com/watch?v=QRS8MkLhQmM'
        video_info = self.get_video_info(test_url, flatten=False, writesubtitles='true', subtitleslangs='it,fr')['info']
        requested_subs = video_info['requested_subtitles']
        self.assertEqual(set(requested_subs.keys()), {'it', 'fr'})

    def test_flatten(self):
        test_url = 'http://vimeo.com/56015672'
        info = self.get_video_info(test_url)
        videos = info['videos']
        video_info = videos[0]
        self.assertIsInstance(video_info, dict)

    def test_errors(self):
        resp = self.app.get('/api/info?%s' % compat_urllib_parse.urlencode({'url': 'http://www.google.com'}))
        self.assertEqual(resp.status_code, 500)
        info = json.loads(resp.data.decode(resp.charset))
        self.assertIn('error', info)

        resp = self.app.get('/api/info?%s' % compat_urllib_parse.urlencode({'url': 'foo', 'playlistreverse': 'invalid'}))
        self.assertEqual(resp.status_code, 400)
        info = json.loads(resp.data.decode(resp.charset))
        self.assertIn('error', info)

    def test_extractors(self):
        resp = self.get_json('/api/extractors')
        ies = resp['extractors']
        self.assertIn('youtube', (ie['name'] for ie in ies))

if __name__ == '__main__':
    unittest.main()
