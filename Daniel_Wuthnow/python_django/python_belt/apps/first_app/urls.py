from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
	url(r'^$', views.index),   # This line has changed!
	url(r'^home', views.home),
	url(r'^register', views.register),
	url(r'^login', views.login),
	url(r'^logout', views.logout),
	url(r'add$', views.add),
	url(r'add/trip$', views.add_trip),

]