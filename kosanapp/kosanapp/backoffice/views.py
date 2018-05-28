from django.contrib.auth import login as django_login, logout as django_logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

def index(request):
	form = AuthenticationForm(data=request.POST or None)
	if form.is_valid():
		django_login(request,form.get_user())
		return redirect("backoffice:menu:home")
	context_data = {
		"form" : form
	}
	return render(request,'index.html',context_data)

def logout(request):
	django_logout(request)
	return redirect("backoffice:index")
