from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
	response = "Plasceholder to later display all the list of blogs"
	return HttpResponse(response)

def new(request):
	response = "This is a Plasceholder to display a new form to create a new blog"
	return HttpResponse(response)

def create(request):
	return redirect('/blogs')

def show(request, number):
	response = "Plasceholder for blog "+number
	return HttpResponse(response)

def edit(request, number):
	response = "Plasceholder to edit blog "+number
	return HttpResponse(response)

def destroy(request):
	return redirect('/blogs')

def home(request):
	return redirect('/blogs')