from django.shortcuts import render,redirect
from kosanapp.apps.kelola.models import query_kosan
from kosanapp.backoffice.kelola.forms import KelolaForm
from django.contrib import messages

def index(request):
	data = query_kosan.objects.all()
	return render(request,'backoffice/kelola/index.html', {"datas":data})

def add(request):
	form = KelolaForm(data=request.POST or None)
	context_data = {"form":form,
					"title":"Tambah Data"}
	if form.is_valid():
		form.save()
		messages.success(request,"Berhasil")
		return redirect('backoffice:kelola:index')
		
	return render(request, 'add.html',context_data)

def edit(request,id):
	kosan = query_kosan.objects.get(id=id)
	form = KelolaForm(data=request.POST or None, instance=kosan)

	if form.is_valid():
		form.save()
		messages.success(request, 'Berhasil diubah')
		return redirect('backoffice:kelola:index')

	context_data = {
		'form': form
	}

	return render(request, 'add.html', context_data)

def delete(request,id):
	query = query_kosan.objects.get(id=id)
	query.delete()
	messages.success(request,"Data Berhasil Dihapus")
	return redirect('backoffice:kelola:index')
	