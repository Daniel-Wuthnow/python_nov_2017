# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
	request.session.clear()
	return render(request, 'first_app/index.html')

def process(request):
	if 'name' not in request.session:
		request.session['name'] = request.POST['name']
	if 'location' not in request.session:
		request.session['location'] = request.POST['location']
	if 'language' not in request.session:
		request.session['language'] = request.POST['language']
	if 'comment' not in request.session:
		request.session['comment'] = request.POST['comment']
	return redirect('/result')

def result(request):
	return render(request, 'first_app/result.html')

# def process(request):
