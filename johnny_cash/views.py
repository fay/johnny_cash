import datetime

from django.shortcuts import render
from django.views.decorators.cache import cache_control

def cash(request):
    resp = render(request, "cash.html")
    #resp['last-modified'] = datetime.datetime(year=2016, month=12, day=20)
    #resp['expires'] = datetime.datetime(year=2016, month=12, day=22)
    return resp
