# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from time import gmtime, strftime
from .models import User

# Create your views here.

def index(request):
	if 'user_id' not in request.session:
		return redirect('/')
	if 'errors' not in request.session:
		request.session['errors'] =[]
	contex = {
		'errors': request.session['errors']
	}
	request.session['errors'] = None
	return render(request, 'first_app/index.html', contex)

def home(request):
	# request.session['user_id'] = 3
	if 'user_id' not in request.session:
		return redirect('/')
	contex = {
		'users': User.objects.all(),
		'current_user': User.objects.get(id=request.session['user_id'])
	}
	return render(request, 'first_app/home.html', contex)

def register(request):
	if request.method == "POST":
		errors = User.objects.register_validation(request.POST)
		if len(errors) != 0:
			request.session['errors'] = errors
			return redirect('/')
		else:
			user = User.objects.register(request.POST)
			request.session['user_id'] = user.id
			return redirect('/home')

def login(request):
	if request.method == "POST":
		errors = User.objects.login_validation(request.POST)
		if len(errors) != 0:
			request.session['errors'] = errors
			return redirect('/')
		else:
			user = User.objects.login(request.POST)
			request.session['user_id'] = user.id
			return redirect('/home')

def logout(request):
	request.session.clear()
	return redirect('/')