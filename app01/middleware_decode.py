from django.utils.deprecation import MiddlewareMixin
import json


# 解析POST请求的数据
class Md1(MiddlewareMixin):
    # 请求中间件
    def process_request(self, request):
        if request.method == 'POST' and request.META.get('CONTENT_TYPE') == 'application/json':


            print(request.META.get('CONTENT_TYPE'))
            data = json.loads(request.body)
            request.data = data

    def process_response(self, request, response):
        return response
