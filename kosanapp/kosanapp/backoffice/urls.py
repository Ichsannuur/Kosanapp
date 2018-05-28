from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^menu/', include('kosanapp.backoffice.menu.urls', namespace='menu')),
    url(r'^kelola/', include('kosanapp.backoffice.kelola.urls', namespace='kelola')),
    url(r'^fasilitas/', include('kosanapp.backoffice.fasilitas.urls', namespace='fasilitas'))
]
