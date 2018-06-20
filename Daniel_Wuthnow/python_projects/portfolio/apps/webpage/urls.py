from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
	url(r'^$', views.index),
	url(r'^about_me$', views.about),
	url(r'^contact$', views.contact),
	url(r'^email$', views.email),
]