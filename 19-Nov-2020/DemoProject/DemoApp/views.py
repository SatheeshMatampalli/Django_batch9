from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
def index(request):
	return HttpResponse ("<h2>Welcome Django Workshop</h2>")

def name(request,n):
	n = "Prasanna Raj M"
	return HttpResponse('<h1>Hie This is {} </h1>'.format(n))
def empnumber(request,empno):
	return HttpResponse('My empnumber is {}'.format(empno))

def empdata(request,n,empno):
	return HttpResponse('My name is {},and empumber is {}'.format(n,empno))


def info(request,wish,name,rollnumber):
	wish = "Good Evening"
	name = "Prasanna Raj M"
	rollnumber = 2422
	return HttpResponse('Hello{},My name is{} and roll no is{}'.format(wish,name,rollnumber))

