# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from .models import User
from .forms import UploadFileForm

# Create your views here.

def index(request):
	return render(request, 'first_app/index.html')

def success(request):
	contex = {
		'users': User.objects.all(),
	}
	return render(request, 'first_app/success.html', contex)

def show(request, number):
	contex = {
		'number':number,
		'user':User.objects.get(id=number),
	}
	return render(request, 'first_app/user.html', contex)

def delete(request, number):
	User.objects.user_remove(number)
	return redirect('/success')

def edit(request, number):
	contex = {
		'number':number,
		'user':User.objects.get(id=number),
	}
	return render(request, 'first_app/edit.html', contex)

def update(request, number):
	user = User.objects.get(id=number)
	
	print user.picture
	User.objects.user_edit(request.POST, request.FILES, number)
	print user.id
	return redirect(reverse('show', kwargs={'number':user.id}))

def create_user(request):
	if request.method == 'POST':
		print "test"
		print request.method
		print request
		# file = request.FILES
		user = User.objects.user_add(request.POST, request.FILES)
		return redirect('/success')