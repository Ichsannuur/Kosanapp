from django.contrib import admin
from django.conf.urls import include, url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^backoffice/', include("kosanapp.backoffice.urls", 
        namespace='backoffice')),
]
