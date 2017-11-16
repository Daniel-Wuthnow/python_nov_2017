from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
	url(r'(?P<number>\d+)$', views.show),
	url(r'(?P<number>\d+)/edit$', views.edit),
	url(r'(?P<number>\d+)/delete$', views.destroy),
	url(r'^create', views.create),
	url(r'^new', views.new),
	url(r'^$', views.index)     # This line has changed!
]