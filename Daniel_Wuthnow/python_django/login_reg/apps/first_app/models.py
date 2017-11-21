# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.
class UserManager(models.Manager):

	def register_validation(self, form_data):
		errors = []
		if len(form_data['first_name']) == 0:
			errors.append('First Name required.')
		if len(form_data['last_name']) == 0:
			errors.append('Last Name required.')
		if len(form_data['email']) == 0 or not EMAIL_REGEX.match(form_data['email']):
			errors.append('Email Invalid.')
		if len(form_data['password']) < 8:
			errors.append('Password should have more than 8 characters.')
		if form_data['password'] != form_data['confirm_password']:
				errors.append('Password should match.')	
		duplicate = User.objects.filter(email = form_data['email'])
		if len(duplicate) == 1:
			errors.append('Email taken.')

		return errors


	def register(self, form_data):
		pw = str(form_data['password'])
		hashed_pw = bcrypt.hashpw(pw,bcrypt.gensalt())

		user = User.objects.create(
			first_name = form_data['first_name'],
			last_name = form_data['last_name'],
			email = form_data['email'],
			password = hashed_pw,
		)
		return user

	def login_validation(self, form_data):
		errors= []
		user = User.objects.filter(email=form_data['email']).first()
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
		return user


class User (models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()

	def __unicode__(self):
		return "first_name: {}, last_name: {}, email: {}, id: {}".format(self.first_name, self.last_name, self.email, self.id)

