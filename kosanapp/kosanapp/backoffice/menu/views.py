from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from kosanapp.apps.kelola.models import query_kosan

def home(request):
	count = query_kosan.objects.count()
	context_data = {
		"count" : count
	}
	return render(request,'base.html', context_data)
