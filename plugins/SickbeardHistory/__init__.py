#!/usr/bin/python
# -*- coding: utf-8 -*-

#author: cytec@iamcytec@googlemail.com
# TODO: Lot of stuff, like infos from series and more...

import re
import urllib2, urllib
import json
from plugin import *


#/api/1234/?cmd=history&limit=2
#get last 5 downloads from sickbeard
sb_host = APIKeyForAPI("sickbeard_host")
sb_apikey = APIKeyForAPI("sickbeard_api_key")

class sickBeard(Plugin):   

	res = {
		'getStatus': {
			'de-DE': '.*serien status.*',
			'en-US': '.*(sickbeard|series) status.*',
			'en-GB': '.*(sickbeard|series) status.*'
		},
		'statusSay': {
			'de-DE': 'Deine letzten 5 Downloads:',
			'en-US': 'your last 5 Downloads:',
			'en-GB': 'your last 5 Downloads:'
		}
	}

	@register("de-DE", res['getStatus']['de-DE'])
	@register("en-US", res['getStatus']['en-US'])
	@register("en-GB", res['getStatus']['en-GB'])
	def sb_history(self, speech, language):
		self.say(sickBeard.res['statusSay'][language])
		SearchURL = u''+ sb_host + '/api/' + sb_apikey + '/?cmd=history&limit=5&type=downloaded'
		jsonResponse = urllib2.urlopen(SearchURL).read()
		jsonDecoded = json.JSONDecoder().decode(jsonResponse)
		for entry in jsonDecoded["data"]:
			content = entry["show_name"] + ": " + str(entry["season"]) + "x" + str(entry["episode"])
			self.say(content, ' ')
		self.complete_request()


