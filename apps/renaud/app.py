#!usr/bin/env python
# encoding=utf-8
# maintainer: rgaudin

import rapidsms
from rapidsms.parsers.keyworder import Keyworder

class App(rapidsms.app.App):

    keyword = Keyworder()

    def handle(self, message):

        try:
            func, captures = self.keyword.match(self, message.text)
        except TypeError:
            #message.respond(u"Unrecognised message")
            return False
        try:
            return func(self, message, *captures)
        except Exception, e:
            message.respond(u"System encountered an Error: %s" % e)
            return True

    def old_handle(self, message):
        ''' not used anymore '''
        if message.text.lower().startswith('renaud'):
            message.respond(u"Hello %s" % message.text)
            return True

        return False

    keyword.prefix = ['renaud']
    @keyword(r'(\w+) ([y|n])')
    def renaud(self, message, text, exists):
	if exists == 'y': 
		message.respond(u"Hello %s. Thank you" % text)
	else: 
		message.respond(u"Sorry Massage doesnt exist")
	   		
	return True
    
    keyword.prefix = ['multi', 'product']
    @keyword(r'([0-9]+) ([0-9]+)')
    def multiplication(self, message, first, second ):

        message.respond(u"The result = %s " % (int(first) * int(second)) )
        return True

