# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from .models import User
# Create your views here.
def index(request):
	if 'errors' not in request.session:
		request.session['errors'] =[]
	request.session['errors'] = None
	return redirect('/users')

def users(request):
	contex = {
		'users': User.objects.all(),
	}
	return render(request, 'first_app/home.html', contex)

def new(request):
	return render(request, 'first_app/new.html')

def show(request, id):
	contex = {
		'id':id,
		'user':User.objects.get(id=id),
	}
	return render(request, 'first_app/show.html', contex)

def create(request):
	if request.method == "POST":
		errors = User.objects.user_validator(request.POST)
		print errors
		if len(errors) != 0:
			request.session['errors'] = errors
			return redirect('/users/new')
		else:
			user = User.objects.user_add(request.POST)
			return redirect(reverse("show", kwargs={'id':user.id}))

def destroy(request, id):
	User.objects.user_remove(id)
	return redirect('/users')

def edit(request, id):
	contex = {
		'id':id,
	}
	return render(request, 'first_app/edit.html', contex)

def update(request,id):
	user = User.objects.get(id=id)
	User.objects.user_edit(request.POST, id)
	return redirect(reverse("show", kwargs={'id':user.id}))