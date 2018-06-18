from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
	url(r'^$', views.index),     # This line has changed!
	url(r'^create_user$', views.create_user),
	url(r'^success$', views.success),
	url(r'^success/(?P<number>\d+)$', views.show, name='show'),
	url(r'^destroy/(?P<number>\d+)$', views.delete),
	url(r'^edit/(?P<number>\d+)$', views.edit),
	url(r'^update/(?P<number>\d+)$', views.update),
]