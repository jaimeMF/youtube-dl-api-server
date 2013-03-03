#!/usr/bin/env python

import unittest

import urllib2

import json
import yaml

def getVideoInfo(url, extra_parameters={}):
	par = ""
	for extra_par in extra_parameters:
		par = "&".join((par,"%s=%s" %(extra_par, extra_parameters[extra_par])))
	request_url = "http://localhost:9191/api/?url=%s%s" % (url, par)
	response = urllib2.urlopen(request_url)
	response_str = response.read().decode('utf-8')
	return response_str

class APITest(unittest.TestCase):
	def test_TED(self):
		"""Test video (TED talk)"""
		test_url = "http://www.ted.com/talks/dan_dennett_on_our_consciousness.html"
		dic = json.loads(getVideoInfo(test_url))
		self.assertEqual(dic["url"], test_url)
	def test_YAML(self):
		"""Test yaml responses"""
		test_url = "http://store.steampowered.com/video/105600/"
		video_info = getVideoInfo(test_url, {"format":"yaml"})
		dic = yaml.load(video_info)
		self.assertEqual(dic["url"], test_url)
		self.assertGreaterEqual(len(dic["videos"]),2)
		
if __name__ == '__main__':
	unittest.main()
