#!/usr/bin/python
# -*- coding: utf-8 -*-
# siriServer GoogleVoice Plugin_NODB 1.0 
#Author: SNXRaven (Jonathon Nickols)

from plugin import *
from googlevoice import Voice
from googlevoice.util import input
import re


gemail = APIKeyForAPI("googleemail")
gpass = APIKeyForAPI("googlepass")

class raven_voice(Plugin):


    @register("en-US", "(Message [a-zA-Z0-9]+)")
    def r_gvsms(self, speech, language):
        match = re.match(u"Message (.*\d.*) say (.*\D.*)", speech, re.IGNORECASE)
        phoneNumber = match.group(1)
        text = match.group(2)
        voice = Voice()
        voice.login(gemail, str(gpass))
        voice.send_sms(phoneNumber, text)
        self.say('Your message has been sent!')
        self.complete_request()
