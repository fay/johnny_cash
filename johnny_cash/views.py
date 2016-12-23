import datetime

from django.shortcuts import render
from django.views.decorators.cache import cache_control
from django.views.decorators.cache import cache_page


@cache_page(60)
@cache_control(must_revalidate=True)
def cash(request):
    resp = render(request, "cash.html")
    #resp['last-modified'] = datetime.datetime(year=2016, month=12, day=23)
    #resp['expires'] = datetime.datetime(year=2016, month=12, day=23)
    #resp['Vary'] = 'Cookie'
    return resp
