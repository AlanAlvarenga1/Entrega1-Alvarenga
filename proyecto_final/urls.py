from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path ('',include("blog_django.urls")),
    path ('usuario/',include("usuarios.urls"),name='usuarios'),
    path('admin/', admin.site.urls)
]
