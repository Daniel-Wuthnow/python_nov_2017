from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
	url(r'^$', views.index),     # This line has changed!
	url(r'^register', views.register),
	url(r'^login', views.login),
	url(r'^logout', views.logout),
	url(r'^quotes', views.home),
	url(r'^add_quote', views.add),
	url(r'^users', views.users),
	url(r'^add_fav', views.add_fav),
	url(r'^remove_fav', views.remove_fav),
]