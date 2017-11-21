from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
	url(r'^clear', views.clear),
	url(r'^session_words', views.word),
	url(r'^$', views.index)     # This line has changed!
]