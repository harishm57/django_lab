from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime,timedelta

def current_datetime(request):
    now=datetime.now()
    ahead=now+timedelta(hours=4)
    before=now-timedelta(hours=4)
    html="<html><body><h1>Current date and time:{0},<br> four hours ahead:{1}<br> four hours before:{2}</h1></body></html>".format(now,ahead,before)
    return HttpResponse(html)
