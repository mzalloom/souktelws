#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4 coding=utf-8
# Mohannad Zalloom

''' DB file which creates the Table for our survey program '''

from django.db import models
from django.utils.translation import ugettext_lazy as _



class Activities(models.Model) :
    ''' Creates Activity model

    stores the types of Activities we have in system'''
    code = models.CharField(max_length=5, unique=True, verbose_name=_(u"Code"))
    name= models.CharField(max_length=20, verbose_name=_(u"Name"))

    def __unicode__(self):
	    return u"%s (%s)"% (self.code,self.name)



class Profile(models.Model) :
    ''' This Profile model

    Stores information about the users of the system'''

    First_Name = models.CharField(max_length=20, unique=True, verbose_name=_(u"First Name"))
    Last_Name = models.CharField(max_length=20, verbose_name=_(u"Last Name"))
    Sex	= models.CharField(max_length=1, verbose_name=_(u"Sex"))
    Age = models.CharField(max_length=5, verbose_name=_(u"Age"))
    Activity = models.ForeignKey(Activities)
    
    def __unicode__(self):
            return u"%s (%s) (%s) (%s)"% (self.First_Name,self.Last_Name,self.Sex,self.Age)

