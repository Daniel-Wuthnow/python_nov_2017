# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import User, Quote


# Create your views here.
def index(request):
	if 'errors' not in request.session:
		request.session['errors'] =[]
	contex = {
		'errors': request.session['errors']
	}
	request.session['errors'] = None
	return render(request, "first_app/main.html", contex)

def home(request):
	if 'user_id' not in request.session:
		return redirect('/')
	contex = {
		'users': User.objects.all(),
		'current_user': User.objects.get(id=request.session['user_id']),
		'quotes' : Quote.objects.all(),		
	}
	return render(request, 'first_app/quotes.html', contex)

def users(request):
	if 'user_id' not in request.session:
		return redirect('/')
	# request.session['post_id'] = User.objects.all().id
	request.session['post_id'] = User.objects.all()[1].id
	# print test
	contex = {
		'quotes' : Quote.objects.all(),
		'users' : User.objects.get(id=request.session['post_id'])
	}
	return render(request, 'first_app/users.html', contex)

def register(request):
	if request.method == "POST":
		errors = User.objects.register_validation(request.POST)
		if len(errors) != 0:
			request.session['errors'] = errors
			return redirect('/')
		else:
			user = User.objects.register(request.POST)
			request.session['user_id'] = user.id
			return redirect('/quotes')

def login(request):
	if request.method == "POST":
		errors = User.objects.login_validation(request.POST)
		if len(errors) != 0:
			request.session['errors'] = errors
			return redirect('/')
		else:
			user = User.objects.login(request.POST)
			request.session['user_id'] = user.id
			return redirect('/quotes')

def logout(request):
	request.session.clear()
	return redirect('/')

def add(request):
	if request.method == "POST":
		quote = Quote.objects.add_quote(request.POST)
		return redirect('/quotes')

def add_fav(request):
	return redirect('/quotes')

def remove_fav(request):
	return redirect('/quotes')

