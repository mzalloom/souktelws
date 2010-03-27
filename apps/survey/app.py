#!usr/bin/env python
# encoding=utf-8
# Mohannad Zalloom

''' This is An Small Survey Example '''

import rapidsms
from rapidsms.parsers.keyworder import Keyworder
from models import Profile, Activities

from django.utils.translation import ugettext as _

 

class App(rapidsms.app.App):
    '''   '''

    keyword = Keyworder()

    def handle(self, message):
        ''' Searchs for the right function and then call it '''
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
          
    keyword.prefix = ['Help', _(u"help")] 
    @keyword(r'')

    def help(self, message):
        ''' Displays how to use the commands '''
        message.respond(_(u"Please enter the follow info [Surname,Name,Sex,Age(M:Male,F:Female),Acitivity(ST:Student,WR:Worker)]"))
        return True
    
    keyword.prefix = ['survey', _(u"survey")]
    @keyword(r'([a-z]+) ([a-z]+) ([M|F]) ([0-9]+) ([a-z]+)')
  
    def survey(self, message, first, last, sex, age, Act):
        ''' receivces from the user the requisted data to be inserted in DB '''

        # create profile from data
        Act1 = Activities.objects.get(code =Act)
        prof = Profile(First_Name = first, Last_Name = last, Sex = sex, Age = age, Activity = Act1)

        # save the profile
        try : 
            prof.save()
            message.respond(_(u"success"))
        except:
            message.repond(_(u"Error"))
            
        return True

    keyword.prefix = ['find', _(u"find")]
    @keyword(r'([a-z]+)')
    
    def find(self, message , keyw):
        ''' simple search program which displays the First Name in DB related to you input '''
        Act1 = Activities.objects.get(code =keyw)
        prof1 = Profile.objects.get(Activity=Act1)

        message.respond(_(u"Hello %s") % prof1.First_Name)

        return True

#stat function // gives the no of records stored in DB
         
    keyword.prefix = ['stat', _(u"stat")]
    @keyword(r'')
    def stat(self, message):
        
        message.respond(_(u"Number of Records %s") % Profile.objects.count())


        return True