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
			name=postData['name'],
			username=postData['username'],
			password=hashed_pw,
		)
		return user

	def register_validation(self, postData):
		errors = []
		if len(postData['name'])<3:
			errors.append('You need a name!')
		if len(postData['username'])<3:
			errors.append('You need a username!')
		duplicate = User.objects.filter(username = postData['username'])
		if len(duplicate) == 1:
			errors.append('username taken.')
		if len(postData['password']) < 8:
			errors.append('Password must be atleast 8 charactores.')
		if postData['password'] != postData['con_password']:
			errors.append('Passwords do not match.')
		return errors

	def login(self, postData):
		user = User.objects.filter(username=postData['username']).first()
		return user

	def login_validation(self, postData):
		errors = []
		user = User.objects.filter(username=postData['username']).first()
		if user:
			pw = str(postData['password'])
			user_password = str(user.password)
			hashed_pw = bcrypt.hashpw(pw,user_password)
			if user_password != hashed_pw:
				errors.append('Invalid Password.')
		else:
			errors.append('Invalid username.')
		return errors


class User(models.Model):
	name = models.CharField(max_length=40)
	username = models.CharField(max_length=40)
	password = models.CharField(max_length=40)
	hired = models.DateTimeField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()

	def __unicode__(self):
		return "name: {}, username: {}, id: {}".format(self.name, self.username, self.id)