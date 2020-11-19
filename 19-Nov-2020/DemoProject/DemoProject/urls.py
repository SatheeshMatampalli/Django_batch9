"""DemoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from DemoApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index,name="index"),# Function Based Views
    path('name/<str:n>/',views.name,name="name"),
    path('empnumber/<int:empno>/',views.empnumber,name="empnumber"),
    path('empdata/<str:n>/<int:empno>/',views.empdata,name='empdata'),
    path('info/<str:wish>/<str:name>/<int:rollnumber>/',views.info,name="info"),

]
