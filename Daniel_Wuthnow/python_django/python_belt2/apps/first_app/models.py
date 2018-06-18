# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import datetime
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):

	def register_validation(self, form_data):
		errors = []
		if len(form_data['name']) < 3:
			errors.append('Name required.')
		if len(form_data['alias']) < 3:
			errors.append('Alias required.')
		if len(form_data['password']) < 8:
			errors.append('Password should have more than 8 characters.')
		if form_data['password'] != form_data['confirm_password']:
				errors.append('Password should match.')	
		duplicate = User.objects.filter(alias = form_data['alias'])
		if len(duplicate) == 1:
			errors.append('Alias taken.')
		return errors

	def register(self, form_data):
		pw = str(form_data['password'])
		hashed_pw = bcrypt.hashpw(pw,bcrypt.gensalt())

		user = User.objects.create(
			name = form_data['name'],
			alias = form_data['alias'],
			password = hashed_pw,
		)
		return user

	def login_validation(self, form_data):
		errors= []
		user = User.objects.filter(email=form_data['email']).first()
		print user
		if user:
			pw = str(form_data['password'])
			user_password = str(user.password)
			hashed_pw = bcrypt.hashpw(pw,user_password)
			if user_password != hashed_pw:
				errors.append('Invalid Password.')
		else:
			errors.append('Invalid Email.')
		return errors

	def login(self, form_data):
		user = User.objects.filter(email=form_data['email']).first()
		print user
		return user

	def has_numbers(inputString):
		return any(char.isdigit() for char in inputString)

class User(models.Model):
	name = models.CharField(max_length=38)
	alias = models.CharField(max_length=38)
	email = models.CharField(max_length=38)
	password = models.CharField(max_length=38)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()
  
	def __unicode__(self):
		return "id: " + str(self.id) + ", email: " + self.email

class QuoteManager(models.Manager):
	def add_quote(self, form_data):
		quote = Quote.objects.create(
			quoted_by = form_data['quoted_by'],
			quote = form_data['quote']
		)
		return quote

	def add_quote_fav(self, form_data):
		pass

class Quote(models.Model):
	quoted_by = models.CharField(max_length=38)
	quote = models.CharField(max_length=255)
	users = models.ManyToManyField(User, related_name="quotes")
	user = models.ForeignKey(User, related_name="many_quotes")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = QuoteManager()

	def __unicode__(self):
		return "quoted_by: {}, quote: {}, id: {}".format(self.quoted_by, self.quote, self.id)