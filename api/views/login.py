from django import forms
from django.contrib import auth
from app01.models import UserInfo
from django.views import View
from django.http import JsonResponse


# CBV class
# FBV function

class LoginBaseForm(forms.Form):
    name = forms.CharField(error_messages={'required': '请输入用户名'})
    pwd = forms.CharField(error_messages={'required': '请输入密码'})
    code = forms.CharField(error_messages={'required': '请输入验证码'})

    # 重新init方法
    def __init__(self, *args, **kwargs):
        # 做自己想做的事情
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    # 局部钩子
    def clean_code(self):
        code: str = self.cleaned_data.get('code')
        valid_code: str = self.request.session.get('valid_code')
        if code.upper() != valid_code.upper():
            self.add_error('code', '验证码输入错误')
        return self.cleaned_data


# 登陆的字段验证
class LoginForm(LoginBaseForm):

    # 全局钩子
    def clean(self):
        name = self.cleaned_data.get('name')
        pwd = self.cleaned_data.get('pwd')

        user = auth.authenticate(username=name, password=pwd)
        if not user:
            # raise ValidationError('用户名或密码错误')
            # 为字段添加错误信息
            self.add_error('pwd', '用户名或密码错误')
            return self.cleaned_data

        # 把用户对象放到cleand_data中
        self.cleaned_data['user'] = user
        return self.cleaned_data


# 注册字段验证
class SignForm(LoginBaseForm):
    re_pwd = forms.CharField(error_messages={'required': '请输入确认密码'})

    def clean(self):
        pwd = self.cleaned_data.get('pwd')
        re_pwd = self.cleaned_data.get('re_pwd')
        if pwd != re_pwd:
            self.add_error('re_pwd', '两次密码不一致')
            return self.cleaned_data

    def clean_name(self):
        name = self.cleaned_data.get('name')
        user_query = UserInfo.objects.filter(username=name)
        if user_query:
            self.add_error('name', '该用户已注册')
        return self.cleaned_data


# 登陆失败的可复用代码
def clean_form(form):
    err_dict: dict = form.errors
    # 拿到所有的错误字段名字
    err_valid = list(err_dict.keys())[0]
    # 拿到的第一个字段的第一个错误信息
    err_msg = err_dict[err_valid][0]
    # print(err_dict['name'][0])
    # print(err_valid, err_msg)
    return err_valid, err_msg


# CBV
class LoginView(View):
    def post(self, request):
        res = {
            'code': 425,
            'msg': "登陆成功",
            'self': None
        }
        form = LoginForm(request.data, request=request)
        if not form.is_valid():
            # 验证不通过
            res['self'], res['msg'] = clean_form(form)
            return JsonResponse(res)

        # 执行我们的登录操作
        user = form.cleaned_data.get('user')
        auth.login(request, user)
        res['code'] = 0
        return JsonResponse(res)


class SignView(View):
    def post(self, request):
        res = {
            'code': 425,
            'msg': "注册成功",
            'self': None
        }
        form = SignForm(request.data, request=request)
        if not form.is_valid():
            # 验证不通过
            res['self'], res['msg'] = clean_form(form)
            return JsonResponse(res)
        # 注册成功的代码
        user = UserInfo.objects.create_user(
            username=request.data.get('name'),
            password=request.data.get('pwd')
        )
        # 注册之后直接登录
        auth.login(request, user)
        res['code'] = 0

        return JsonResponse(res)
