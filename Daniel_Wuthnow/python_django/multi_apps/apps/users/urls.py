from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
	url(r'^users/new$', views.new),
	url(r'^users$', views.users),
	url(r'^login$', views.login),
	url(r'^register$', views.register),     # This line has changed!
]