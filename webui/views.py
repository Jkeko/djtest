# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render
from django.http import HttpResponse , JsonResponse,HttpResponseRedirect
from django.shortcuts import render
# Create your views here.
from view_model.jd_promo_unittest import Promo
def hello(request):
    return HttpResponse("Hello world ! From test_mgmt App ")
def send_html(request):
    return render(request,'send.html')

def send_bonus(request):
 ld = Promo().send_bonus()
 return HttpResponse(content_type='application/json', content=json.dumps({'返回值': ld}))

