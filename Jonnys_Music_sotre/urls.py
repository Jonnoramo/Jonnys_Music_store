"""Jonnys_Music_sotre URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from accounts import views as accounts_views
from blog import views as blog_views
from products import views as product_views
from hello import views
from music import views as music_views
from thread import views as thread_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/$', accounts_views.register, name='register'),
    url(r'^profile/$', accounts_views.profile, name='profile'),
    url(r'^login/$', accounts_views.login, name='login'),
    url(r'^logout/$', accounts_views.logout, name='logout'),   
    url(r'^products/$', product_views.all_products),
    url(r'^music/$', music_views.all_music),
    url(r'^blog$', blog_views.post_list, name="post_list"),
    url(r'^blog/$', blog_views.post_list, name="post_list"),
    url(r'^blog/(?P<id>\d+)/$', blog_views.post_details, name="post_details"),
    url(r'^blog/post/$', blog_views.new_post, name='new_post'),
    url(r'^forum/$', thread_views.forum, name='forum'),
    url(r'^threads/(?P<subject_id>\d+)/$', thread_views.threads, name='threads'),
    url(r'^new_thread/(?P<subject_id>\d+)/$', thread_views.new_thread, name='new_thread'),
    url(r'^thread/(?P<thread_id>\d+)/$', thread_views.thread, name='thread'),
    url(r'^post/new/(?P<thread_id>\d+)/$', thread_views.new_post, name='new_post'),
    url(r'^post/edit/(?P<thread_id>\d+)/(?P<post_id>\d+)/$', thread_views.edit_post, name='edit_post'),
    url(r'^post/delete/(?P<post_id>\d+)/$', thread_views.delete_post, name='delete_post'),
    url(r'^thread/vote/(?P<thread_id>\d+)/(?P<subject_id>\d+)/$', thread_views.thread_vote, name='cast_vote'),
    url('', include('hello.urls')),
    url('', include('contact.urls')),
    url('', include('paypal_store.urls')),
    url('', include('threads.urls')),
]
