from django.contrib import admin
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^email/$', views.emailView, name='email'),
    url(r'^success/$', views.successView, name='success'),
]