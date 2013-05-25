#!/usr/bin/env python

import unittest

import urllib2

import webapp2

import json
import yaml

from youtube_dl_server import app


def getVideoInfo(url, extra_parameters={}):
    par = ""
    for extra_par in extra_parameters:
        par = "&".join((par, "%s=%s" % (extra_par, extra_parameters[extra_par])))
    request_url = "http://localhost:9191/api/?url=%s%s" % (url, par)
    response = urllib2.urlopen(request_url)
    response_str = response.read().decode('utf-8')
    return response_str


class ServerTest(unittest.TestCase):
    def skip_if_conection_refused(self, error):
        """
        Skip if the connection was refused
        """
        if "refused" in str(error.reason):
            self.skipTest("Connection refused")
        else:
            raise error

    def test_TED(self):
        """Test video (TED talk)"""
        test_url = "http://www.ted.com/talks/dan_dennett_on_our_consciousness.html"
        try:
            dic = json.loads(getVideoInfo(test_url))
        except urllib2.URLError as e:
            self.skip_if_conection_refused(e)
        self.assertEqual(dic["url"], test_url)

    def test_YAML(self):
        """Test yaml responses"""
        test_url = "http://store.steampowered.com/video/105600/"
        try:
            video_info = getVideoInfo(test_url, {"format": "yaml"})
        except urllib2.URLError as e:
            self.skip_if_conection_refused(e)
        dic = yaml.load(video_info)
        self.assertEqual(dic["url"], test_url)
        self.assertGreaterEqual(len(dic["videos"]), 2)


class RequestHandlerTest(unittest.TestCase):
    def test_handler(self):
        """
        Test the API handler
        Without running a server
        """

        test_url = 'http://www.ted.com/talks/dan_dennett_on_our_consciousness.html'
        request = webapp2.Request.blank("/api/?url=%s" % test_url)

        response = request.get_response(app)

        self.assertEqual(response.status_int, 200)
        dic = json.loads(response.body)
        self.assertEqual(dic["url"], test_url)

if __name__ == '__main__':
    unittest.main()
