from django import template

# 注册
register = template.Library()

# 自定义过滤器
# @register.filter()
# def add(item):
#     return int(item) + 1


@register.inclusion_tag('my_tag/headers.html')
def banner(menu_name):
    img_list = [
        "https://pic3.zhimg.com/v2-2eca64da78d43daca1e085c5a7688b3c_r.jpg",
        "https://pic3.zhimg.com/v2-b0426ba07f6acc832a4b4a196c4ebfcc_r.jpg?source=1940ef5c",
        "https://pic2.zhimg.com/v2-7aad9606b141ad7039e70009a0ed88c1_r.jpg",
        "https://pic2.zhimg.com/v2-24dfbd91377c5d17333b0a9f5cddea84_r.jpg?source=1940ef5c"
    ]
    return {"img_list": img_list}