#!/usr/bin/python
# -*- coding: utf-8 -*-
# author: cytec@iamcytec@googlemail.com
# unnützes wissen / random german qoutes/fakts

from plugin import *
import urllib
import re
from BeautifulSoup import BeautifulSoup

class wissen(Plugin):
	res = {
        'wissen': {
            'de-DE': '.*wissen.*'
        },
        'zitat': {
            'de-DE': '.*zitat.*'
        }
    }

	@register("de-DE", res['wissen']['de-DE'])
	def wissen_get(self, speech, language):
		html = urllib.urlopen("http://unnuetzeswissen.info/zufaelliges-wissen.php").read()
		soup = BeautifulSoup(html)
		zitat = soup.blockquote.p.b.text
		self.say(zitat)
		self.complete_request()

	@register("de-DE", res['zitat']['de-DE'])
	def zitat_get(self, speech, language):
		html = urllib.urlopen("http://www.zitate-online.de/zufallszitat.txt.php").read()
		soup = BeautifulSoup(html)
		zitat = soup.div.text.replace("vonzitate-online.de", "").replace("&bdquo;" , "\"").replace("&ldquo;", "\"").replace("&auml;", "ä")
		self.say(zitat)
		self.complete_request()

