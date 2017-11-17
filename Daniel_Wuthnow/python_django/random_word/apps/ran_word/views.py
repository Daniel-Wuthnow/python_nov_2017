# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):

	return render(request, 'ran_word/index.html')

def generate(request):
	new_word = get_random_string(length=5)
	if 'attempt' not in request.session:
		request.session['attempt'] = 0
	request.session['attempt'] += 1
	contex = {
		"word" : new_word
	}
	return render(request, 'ran_word/index.html', contex)

def clear(request):
	del request.session['attempt']
	return render(request, 'ran_word/index.html')
	