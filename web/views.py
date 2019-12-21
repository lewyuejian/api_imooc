from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse
import json


def Login(request):
    if request.method == 'POST':
        result = {}
        username = request.POST.get('username')
        moblie=request.POST.get('password')
        result['user'] = username
        result['moblieNum'] = moblie
        result = json.dumps(result)
        return HttpResponse(result,content_type='application/json;charset=utf-8')
    else:
        return render(request,'login.html',locals())