"""
URL configuration for v4_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from app01 import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.index),
    path('news/', views.news),
    path('login/', views.login),
    path('login/random_code/', views.get_random_code),
    path('sign/', views.sign),
    path('logout/', views.logout),

    re_path(r'^api/', include('api.urls')),  # 路由分发，将所有以api开头的请求分发到api这个urls.py中
]
