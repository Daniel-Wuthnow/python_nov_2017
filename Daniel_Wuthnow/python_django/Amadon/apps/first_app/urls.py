from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
	url(r'^Amadon$', views.index),     # This line has changed!
	url(r'^Amadon/checkout$', views.checkout),
	url(r'^add$', views.add),
	url(r'^clear$', views.clear),
	url(r'^back$', views.back),
]