from django.shortcuts import render
from .forms import BooksForm
from .models import Books
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
from BookBoom import settings

# Create your views here.
def register(request):
	form=BooksForm(request.POST,request.FILES)
	if form.is_valid():
		form.save()
		#return HttpResponse('Done')
		messages.success(request,request.POST['BookName']+'Added Successfully')

	form=BooksForm()
	return render(request,'FirstApp/register.html',{'form':form})

def show(request):
	data=Books.objects.all()
	return render(request,'FirstApp/show.html',{'data':data})

def message(request):
	if request.method=='POST':
		toemail=request.POST['email']
		sub=request.POST['sub']
		meg=request.POST['meg']
		sender=settings.EMAIL_HOST_USER
		receiver=toemail
		send_mail(sub,meg,sender,[receiver])

		return HttpResponse('Email Send Successfully')

	return render(request,'FirstApp/message.html')