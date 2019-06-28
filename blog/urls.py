from django.contrib import admin
from django.conf.urls import url
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^new/', views.new, name="new"),
    url(r'^(?P<post_id>\d+)/$', views.show, name="show"),
    url(r'^delete/(?P<post_id>\d+)/$', views.delete, name="delete"),
    url(r'^edit/(?P<id>\d+)/$', views.edit, name="edit"),
    url(r'^commentcreate/(?P<pk>\d+)/$', views.commentcreate, name='commentcreate'),
    url(r'^follow/(?P<id>\d+)/$', views.postfollow, name="follow"),
]