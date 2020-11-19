from django.urls import path
from DemoApp import views

urlpatterns = [
    
    path('index/',views.index,name='index')
    
    ]