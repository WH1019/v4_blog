from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from app01.utils.random_code import random_code
from django import forms
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
from django.contrib import auth
from app01.models import UserInfo


# Create your views here.
def index(request):
    return render(request, 'index.html', {'request': request})


def news(request):
    return render(request, 'news.html')





def login(request):
        # name = data.get('name')
        # if not name:
        #     res['msg'] = '请输入用户名'
        #     res['self'] = 'name'
        #     return JsonResponse(res)
        # pwd = data.get('pwd')
        # if not pwd:
        #     res['msg'] = '请输入密码'
        #     res['self'] = 'pwd'
        #     return JsonResponse(res)
        # code = data.get('code')
        # if not code:
        #     res['msg'] = '请输入验证码'
        #     res['self'] = 'code'
        #     return JsonResponse(res)
        #
        # valid_code:str = request.session.get('valid_code')
        # if valid_code.upper() != code.upper():
        #     res['msg'] = '验证码输入错误'
        #     res['self'] = 'code'
        #     return JsonResponse(res)
        # # 校验用户名和密码
        # if name != 'wanghao' or pwd != '1234':
        #     res['msg'] = '用户名密码错误'
        #     res['self'] = 'pwd'
        #     return JsonResponse(res)
    return render(request, 'login2.html')


def sign(request):
    return render(request, 'sign.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


# 获取随机验证码
def get_random_code(request):
    data, valid_code = random_code()
    request.session['valid_code'] = valid_code
    return HttpResponse(data)
