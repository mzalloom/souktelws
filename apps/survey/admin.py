#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4


from django.contrib import admin
from survey.models import *
from models import Profile, Activities

class ProfilesAdmin(admin.ModelAdmin): 
	ordering = [('First_Name') , ('Age') ]
	search_fields = ('First_Name', 'Last_Name', 'Sex', 'Age', 'Activity')
	list_display = ('First_Name', 'Last_Name', 'Sex', 'Age', 'Activity')
	list_filter = ('First_Name', 'Last_Name', 'Sex', 'Age', 'Activity')

admin.site.register(Activities)
admin.site.register(Profile, ProfilesAdmin)
