from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request,'firstapp/Home.html',{})

def css(request):
	return render(request,'firstapp/cssfile.html',{})

def jsalert(request):
	return render(request,'firstapp/jsfile.html',{})