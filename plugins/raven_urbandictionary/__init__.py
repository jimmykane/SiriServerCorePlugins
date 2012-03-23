#!/usr/bin/python
# -*- coding: utf-8 -*-
# siriServer urbandictionary for siriServer v1.0
#Author: SNXRaven (Jonathon Nickols)

import urllib2
import json
import re
from plugin import *

class urbandictionary(Plugin):

    # Dictionary for help phrases used by the helpPlugin
    helpPhrases = {
        "en-US": ["Urban dictionary <something>", "Example: Urban dictionary banana"]
                  }

    @register("en-US", ".*Urban.*dictionary.* [a-zA-Z0-9]+")
    def sn_dictionary(self, speech, language):
        if language == 'en-US':
            match = re.match(u".*Urban.*dictionary (.*\D.*)", speech, re.IGNORECASE)
            r = urllib2.urlopen('http://www.urbandictionary.com/iphone/search/define?term='+match.group(1))
            data = json.loads(r.read())
            if ( len(data['list']) > 1 ):
                data['list'] = data['list'][:1]  # only print 2 results
            for i in range(len(data['list'])):
                word = data['list'][i][u'word']
            definition = data['list'][i][u'definition']
            example = data['list'][i][u'example']
            print(word + ': ' + definition),
            print('example: ' + example),
        self.say(word + ': ' + definition)
        self.say('For example: ' + example)
        self.complete_request()
