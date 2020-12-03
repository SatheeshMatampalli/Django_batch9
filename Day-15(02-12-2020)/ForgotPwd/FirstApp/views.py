from django.shortcuts import render,redirect
from django.core.mail import send_mail
from ForgotPwd import settings
import random
from FirstApp.models import StudentData
from django.http import HttpResponse
# Create your views here.
def register(request):
	if request.method=='POST':
		fname=request.POST['fname']
		lname=request.POST['lname']
		college=request.POST['college']
		email=request.POST['email']
		password=str(random.randint(10000,99999))+lname[2:]
		StudentData.objects.create(First_Name=fname,Last_Name=lname,
			College=college,Email=email,Password=password)
		sub='Reg to your Login Details'
		link='http://127.0.0.1:8000/change'
		body="""Hello {}\n\n This is your UserName {}
		\n\n Your Password {} 
		\n\nYou can Password use this link {}""".format(fname,email,password,link)

		sender=settings.EMAIL_HOST_USER
		receiver=email
		send_mail(sub,body,sender,[receiver])
		return HttpResponse('Done')
	return render(request,'FirstApp/register.html')

def login(request):
	if request.method=='POST':
		uname=request.POST['email']
		pwd=request.POST['password']
		data=StudentData.objects.all().filter(Email=uname,
			Password=pwd)

		if data:
			return HttpResponse('Welcome to '+uname)
		else:
			return HttpResponse('Invalid User')

	return render(request,'FirstApp/login.html')

def forgot(request):
	if request.method=='POST':
		data=StudentData.objects.get(Email=request.POST['email'])
		sub='Reg to your Password info'
		body='Your Password is :'+data.Password
		sender=settings.EMAIL_HOST_USER
		receiver=request.POST['email']
		send_mail(sub,body,sender,[receiver])
		return HttpResponse('Check Your Mail for Password')
	return render(request,'FirstApp/forgot.html')

def change(request):
	if request.method=='POST':
		oldpwd=request.POST['oldpwd']
		newpwd=request.POST['newpwd']
		conpwd=request.POST['conpwd']
		data=StudentData.objects.get(Password=oldpwd)
		if newpwd != conpwd:
			return HttpResponse("Password Does't Match")
		else:
			data.Password=conpwd
			data.save()
			return redirect('/login')

	return render(request,'FirstApp/change.html')