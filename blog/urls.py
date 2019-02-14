from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name="blog_post_list"),
    url(r'^(?P<db_id>\d+)/$', views.post_detail, name="blog_post_detail"),
    url(r'^post/$', views.new_post, name='blog_new_post'),
]