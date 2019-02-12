from django.contrib import admin
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.get_index, name='index'),
    url(r'^about/$', views.get_about, name='about'),
]