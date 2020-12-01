from django.shortcuts import render,redirect
from django.http import HttpResponse
from firstapp.forms import RegisterForm
# Create your views here.

def Reg(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		#print("hai")
		if form.is_valid():
			#print("Hai2")
			form.save()
			return HttpResponse("Registered Sucessfully")
	form = RegisterForm()
	return render(request, 'firstapp/index.html',{'form': form})