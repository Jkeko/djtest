# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.http import HttpResponse , JsonResponse,HttpResponseRedirect
from django.shortcuts import render
from view_model.jd_promo_unittest import Promo
def index(request):
    return render(request, 'send.html')
def hello(request):
    return HttpResponse("Hello world ! From test_mgmt App ")
def send_html(request):
    return render(request,'send.html')
def send_bonus(request):
    ld = Promo().send_bonus
    return HttpResponse(content_type='application/json;charset=UTF-8', content=json.dumps({'返回值': ld}))

def send_coupon(request):
    phone = request.GET.get('phone')
    ld = Promo().send_coupon
    # print(ld)
    # return HttpResponse(ld)
    # return HttpResponse(content_type='application/json', content=json.dumps({'返回值': ld}))
    return render(request, 'ok.html',{'username': phone,'username2':ld})



def serch_offer(request):
    ld = Promo().serch_bonus()
    print(ld)
    # return HttpResponse(content_type='application/json', content=json.dumps({'返回值': ld}))
    return HttpResponse(ld)
