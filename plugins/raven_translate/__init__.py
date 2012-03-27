#!/usr/bin/python
# -*- coding: utf-8 -*-
#Author: SNXRaven (Jonathon Nickols)
# This requires that you have installed bingtrans module from: https://github.com/bahn/bingtrans
# This requires that you get your own api key from: http://www.bing.com/developers/
# rewritten/fixed by cytec

import bingtrans
from plugin import *
bing_api_key = APIKeyForAPI("bing")
bingtrans.set_app_id(bing_api_key)

res = {
	'command': {
		'en-US': u'Translate (?P<transword>[^^]+) from (?P<fromlang>[\w]+) to (?P<tolang>[\w]+)',
		'de-DE': u'(Übersetze|Übersetzer|Übersetzen|Translate) (?P<transword>[^^]+) von (?P<fromlang>[\w]+) (nach|in|zu) (?P<tolang>[\w]+)'
	},
	'answer': {
		'en-US': u'Here is your {0} translation for {1}:\n',
		'de-DE': u'Hier ist deine {0} Übersetzung für {1}:\n'
	},
	'languageCodes': {
		'en-US': {
			u'english': 'en',
			u'spanish': 'sp',
			u'french': 'fr',
			u'italian': 'it',
			u'finnish': 'fi',
			u'greek': 'el',
			u'arabic': 'ar',
			u'czech': 'cs',
			u'dutch': 'nl',
			u'hebrew': 'he',
			u'russian': 'ru',
			u'polish': 'pl',
			u'portuguese': 'pt',
			u'romanian': 'ro',
			u'swedish': 'sv',
			u'turkish': 'tr',
			u'indonesian': 'id',
			u'hungarian': 'id',
			u'german': 'de'
		},
		'de-DE': {
			u'englisch': 'en',
			u'spanisch': 'sp',
			u'französisch': 'fr',
			u'italienisch': 'it',
			u'finnisch': 'fi',
			u'griechisch': 'el',
			u'arabisch': 'ar',
			u'tschechisch': 'cs',
			u'holländisch': 'nl',
			u'hebräisch': 'he',
			u'russisch': 'ru',
			u'polnisch': 'pl',
			u'portugisisch': 'pt',
			u'rumänisch': 'ro',
			u'schwedisch': 'sv',
			u'türkisch': 'tr',
			u'indonesisch': 'id',
			u'ungarisch': 'id',
			u'deutsch': 'de'
		}
	},
	'errors': {
		'en-US': u'I\'m sorry, {0} is not a known language',
		'de-DE': u'Tut mir leid, {0} ist keine Unterstütze Sprache'
	}
}

class bing_translate(Plugin):
	@register('en-US', res['command']['en-US'])
	@register('de-DE', res['command']['de-DE'])
	def snx_translate(self, speech, language, matchedRegex):
		text = matchedRegex.group('transword')
		longlang1 = matchedRegex.group('fromlang').lower()
		longlang2 = matchedRegex.group('tolang').lower()
		try:
			lang1 = res['languageCodes'][language][longlang1]
		except KeyError:
			self.say(res['errors'][language].format(longlang1))
			raise
		try:
			lang2 = res['languageCodes'][language][longlang2]
		except KeyError:
			self.say(res['errors'][language].format(longlang2))
			raise
		self.say(res['answer'][language].format(longlang2, text))
		self.say(bingtrans.translate(text, lang1, lang2, ' '), ' ')
		self.complete_request()
