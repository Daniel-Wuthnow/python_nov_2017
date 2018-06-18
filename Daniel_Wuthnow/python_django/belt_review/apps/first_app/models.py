# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import bcrypt

# Create your models here.
class UserManager(models.Manager):

	def register(self, postData):
		pw = str(postData['password'])
		hashed_pw = bcrypt.hashpw(pw, bcrypt.gensalt())
		user = User.objects.create(
			name = postData['name'],
			alias = postData['alias'],
			email = postData['email'],
			password = hashed_pw,
		)
		return user

	def register_validation(self, postData):
		errors = []
		if len(postData['name']) < 1:
			errors.append('Name required.')
		if len(postData['alias']) < 1:
			errors.append('Alias required.')
		if len(postData['password']) < 8:
			errors.append('Password must be atleast 8 characters.')
		if postData['password'] != postData['comf_password']:
			errors.append('Passwords do not match')
		duplicate = User.objects.filter(alias = postData['alias'])
		if len(duplicate) > 1:
			errors.append('Alias taken')
		return errors


class User(models.Model):
	name = models.CharField(max_length=25)
	alias = models.CharField(max_length=25)
	email = models.CharField(max_length=25)
	password = models.CharField(max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()

	def __unicode__(self):
		return "name: {}, id: {}".format(self.name, self.id)

class Author(models.Model):
	name = models.CharField(max_length=25)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return "Author: {}, id: {}".format(self.name, self.id)

class BookManager(models.Manager):
	def book_author(self, postData):
		if len(postData['author'])==0:
			author=Author.objects.get(name=postData['list'])
		else:
			author=postData['author']
			author = Author.objects.create(
				name=postData['author']
			)
		return author

	def book_add(self, postData, author):
		book = Book.objects.create(
			title=postData['title'],
			author=author
		)
		return book
	

class Book(models.Model):
	title = models.CharField(max_length=25)
	author = models.ForeignKey(Author, related_name='books')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = BookManager()

	def __unicode__(self):
		return "title: {}, author: {}, id: {}".format(self.title, self.author, self.id)

class ReviewManager(models.Manager):

	def review_add(self, postData, user, book):
		review = Review.objects.create(
			ratting = postData['rate'],
			content = postData['review'],
			book = book,
			uploader = user,
		)
		return review


class Review(models.Model):
	ratting = models.IntegerField()
	content = models.CharField(max_length=100)
	book = models.ForeignKey(Book, related_name='reviews')
	uploader = models.ForeignKey(User, related_name='reviews')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = ReviewManager()

	def __unicode__(self):
		return "content: {}, book: {}, uploader: {}, id; {}".format(self.content, self.book, self.uploader, self.id)