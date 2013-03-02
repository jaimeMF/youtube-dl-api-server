#!/usr/bin/env python

import unittest

import urllib2

import json

class APITest(unittest.TestCase):
	def test_TED(self):
		test_url="http://www.ted.com/talks/dan_dennett_on_our_consciousness.html"
		response = urllib2.urlopen("http://localhost:9191/api/?url=%s" % test_url)
		response_str=response.read().decode('utf-8')
		dic=json.loads(response_str)
		self.assertEqual(dic["url"],test_url)
		
if __name__ == '__main__':
	unittest.main()
