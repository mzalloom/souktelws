#!usr/bin/env python
# encoding=utf-8
# Mohannad Zalloom
# This is the Views files

''' we use views to display data in html file '''

from django.http import HttpResponse
from rapidsms.webui.utils import render_to_response
from models import Profile, Activities
from django.contrib.auth.decorators import login_required

def index(request):
    ''' creating objects and make some statistics on them to be displayed in html '''

    all_records = Profile.objects.all()
    total_records = Profile.objects.count()
    No_of_Male = Profile.objects.filter(Sex='M').count()
    No_of_Female = Profile.objects.filter(Sex='F').count()
    
    Act1 = Activities.objects.get(code ='ST')
    No_of_Students = Profile.objects.filter(Activity=Act1).count()
    
    Act2 = Activities.objects.get(code ='WR')
    No_of_Workers = Profile.objects.filter(Activity=Act2).count()

    return render_to_response(request,"survey/index.html",{"records":all_records, "TotalRecords":total_records, "NoOfMale":No_of_Male, 
    "NoOfFemale":No_of_Female, "NoOfStudents":No_of_Students, "NoOfWorkers":No_of_Workers })

@login_required


def profile(request, userid):
    '''Creating object profile and get the users id '''
    
    profile = Profile.objects.get(id=userid)
    return render_to_response(request,"survey/profile.html",{"profile":profile})
