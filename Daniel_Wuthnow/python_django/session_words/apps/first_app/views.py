# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from time import gmtime, strftime

# Create your views here.
def index(request):
	if request.session.get('word') == None:
		request.session['word']=[]
	return render(request, 'first_app/index.html')


temp = []
def word(request):
	if request.POST.get('big') == None:
		class2 = ""
	else:
		class2 = request.POST['big']

	time = strftime("%Y-%m-%d %H:%M %p", gmtime())

	adding_words = {
		"word" : request.POST.get('word'),
		"class1" : request.POST.get('color'),
		"class2" : class2,
		"time" : time
	}
	request.session['word'] = temp
	temp.append(adding_words)
	return redirect('/')

def clear(request):
	request.session.clear()
	return redirect('/')