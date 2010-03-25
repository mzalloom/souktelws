#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4 coding=utf-8
# Mohannad Zalloom


from django.db import models


class Activities(models.Model) :

    code = models.CharField(max_length=5, unique=True)
    name= models.CharField(max_length=20)

    def __unicode__(self):
	    return u"%s (%s)"% (self.code,self.name)

class Profile(models.Model) :

    First_Name = models.CharField("This is First",max_length=20, unique=True)
    Last_Name = models.CharField(max_length=20)
    Sex	= models.CharField(max_length=1)
    Age = models.CharField(max_length=5)
    Activity = models.ForeignKey(Activities)
    
    def __unicode__(self):
            return u"%s (%s) (%s) (%s)"% (self.First_Name,self.Last_Name,self.Sex,self.Age)

