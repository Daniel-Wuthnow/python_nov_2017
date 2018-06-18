from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
	url(r'^$', views.index),     # This line has changed!
	url(r'^register$', views.register),
	url(r'^books$', views.home),
	url(r'^books/add$', views.books_add),
	url(r'^books/(?P<number>\d+)$', views.show, name="show"),
	url(r'^add$', views.add),
	url(r'^add_extra$', views.add_extra),
]