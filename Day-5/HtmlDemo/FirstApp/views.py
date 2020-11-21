from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
	return HttpResponse('Good Evening to All')

def mypage(request):
	return render(request,'FirstApp/mypage.html')

def table(request):
	return render(request,'FirstApp/table.html')

def form(request):
	return render(request,'FirstApp/form.html')