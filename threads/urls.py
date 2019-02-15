from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^forum/$', views.forum, name='forum'),
    url(r'^threads/(?P<subject_id>\d+)/$', views.threads, name='threads'),
    url(r'^new_thread/(?P<subject_id>\d+)/$', views.new_thread, name='new_thread'),
    url(r'^thread/(?P<thread_id>\d+)/$', views.thread, name='thread'),
    url(r'^post/new/(?P<thread_id>\d+)/$', views.new_post, name='new_post'),
    url(r'^post/edit/(?P<thread_id>\d+)/(?P<post_id>\d+)/$', views.edit_post, name='edit_post'),
    url(r'^post/delete/(?P<post_id>\d+)/$', views.delete_post, name='delete_post'),
    url(r'^thread/vote/(?P<thread_id>\d+)/(?P<subject_id>\d+)/$', views.thread_vote, name='cast_vote'),
]   