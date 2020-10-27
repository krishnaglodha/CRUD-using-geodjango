
from django.contrib import admin
from django.urls import path , include #add 'include' to create bridge between mainapp url and project url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls'))
]
