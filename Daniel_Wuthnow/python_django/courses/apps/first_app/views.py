# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Course, Comment

# Create your views here.
def index(request):
	if 'errors' not in request.session:
		request.session['errors'] =[]
	contex = {
		'errors': request.session['errors'],
		'courses': Course.objects.all(),
	}
	request.session['errors'] = None
	return render(request, 'first_app/index.html', contex)

def add(request):
	if request.method == 'POST':
		errors = Course.objects.course_valadation(request.POST)
		if len(errors) != 0:
			request.session['errors'] = errors
			return redirect('/')
		else:
			course = Course.objects.course_add(request.POST)
		return redirect('/')

def destroy(request, number):
	course = Course.objects.get(id=number)
	contex = {
		'course': course
	}
	return render(request, 'first_app/destroy.html', contex)

def delete(request, number):
	Course.objects.course_delete(number)
	return redirect('/')

def comment(request, number):
	course = Course.objects.get(id=number)
	comment = Comment.objects.filter(course=course)
	contex = {
		'course': course,
		'comments':comment,
	}
	return render(request, 'first_app/comment.html', contex)

def comment_add(request, number):
	print number
	course = Course.objects.get(id=number)
	print course
	print request.POST
	comment = Comment.objects.create(
			comment = request.POST['comment'],
			course = course,
		)
	print comment
	return redirect('/')
