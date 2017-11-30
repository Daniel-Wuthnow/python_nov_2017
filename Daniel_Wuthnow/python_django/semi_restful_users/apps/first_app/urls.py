from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
	url(r'^$', views.index),     # This line has changed!
	url(r'^users$', views.users),
	url(r'^users/new$', views.new),
	url(r'^users/create$', views.create),
	url(r'^users/(?P<id>\d+)/update$', views.update),
	url(r'^users/(?P<id>\d+)$', views.show, name="show"),
	url(r'^users/(?P<id>\d+)/destroy$', views.destroy),
	url(r'^users/(?P<id>\d+)/edit$', views.edit),
]