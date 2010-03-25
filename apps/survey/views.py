#!usr/bin/env python
# encoding=utf-8
# Mohannad Zalloom

from django.http import HttpResponse
from rapidsms.webui.utils import render_to_response
from models import Profile, Activities
from django.contrib.auth.decorators import login_required

def index(request):

    all_records = Profile.objects.all()
    total_records = Profile.objects.count()

    return render_to_response(request,"survey/index.html",{"records":all_records, "TotalRecords":total_records})

@login_required
def profile(request, userid):

    profile = Profile.objects.get(id=userid)
    return render_to_response(request,"survey/index.html",{"profile":profile})