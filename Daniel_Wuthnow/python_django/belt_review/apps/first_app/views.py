# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import User, Author, Book, Review
# Create your views here.

def index(request):
	if 'errors' not in request.session:
		request.session['errors'] =[]
	contex = {
		'errors': request.session['errors']
	}
	request.session['errors'] = None
	return render(request, 'first_app/index.html', contex)

def home(request):
	if 'user_id' not in request.session:
		return redirect('/')
	contex = {
		'current_user': User.objects.get(id=request.session['user_id']),
		'user':User.objects.all(),
		'recent_review':Review.objects.order_by('-created_at')[:3],
		'review':Review.objects.all()
	}
	return render(request, 'first_app/books.html', contex)

def register(request):
	if request.method == "POST":
		errors = User.objects.register_validation(request.POST)
		if len(errors) != 0:
			request.session['errors'] = errors
			return redirect('/')
		else:
			user = User.objects.register(request.POST)
			request.session['user_id'] = user.id
			return redirect('/books')

def books_add(request):
	contex = {
		'book': Book.objects.all(),
		'author': Author.objects.all(),
	}
	return render(request, 'first_app/add.html', contex)

def show(request, number):
	contex = {
		'book': Book.objects.get(id=number),
		'review': Review.objects.filter(book=Book.objects.get(id=number))
	}
	return render(request, 'first_app/show.html', contex)

def add(request):
	if request.method == "POST":
		# print request.POST
		author_info = {
			'author':request.POST['author'],
			'list':request.POST['list'],
		}
		author = Book.objects.book_author(author_info)
		print author
		book_info = {
			'title':request.POST['title'],
		}
		book = Book.objects.book_add(book_info, author)
		print book.id
		review_info = {
			'rate':request.POST['rate'],
			'review':request.POST['review']
		}
		print review_info
		user = User.objects.get(id=request.session['user_id'])
		review = Review.objects.review_add(review_info, user, book)
		return redirect(reverse("show", kwargs={'number':book.id}))

def add_extra(request):
	


		
		# book = Book.objects.book_add(request.POST, Book.objects.book_author(request.POST))
		# review = Review.objects.review_add(request.POST, request.session['user_id'], book)