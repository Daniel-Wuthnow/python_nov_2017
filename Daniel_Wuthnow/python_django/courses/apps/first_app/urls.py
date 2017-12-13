from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
	url(r'^$', views.index),     # This line has changed!
	url(r'^add$', views.add),
	url(r'^destroy/(?P<number>\d+)$', views.destroy),
	url(r'^delete/(?P<number>\d+)$', views.delete),
	url(r'^comment/(?P<number>\d+)$', views.comment),
	url(r'^comment/add/(?P<number>\d+)$', views.comment_add),
]