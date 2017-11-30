# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.
class UserManager(models.Manager):
	def user_validator(self, postData):
		errors = {}
		if len(postData['first_name']) < 2 or len(postData['first_name']) < 2:
			errors['name'] = "User name should be more than 2 characters!"
		if len(postData['email']) < 2 or not EMAIL_REGEX.match(postData['email']):
			errors['email'] = "You need to have a valid email!"
		return errors

	def user_add(self, postData):
		user = User.objects.create(
			name = postData['first_name']+ " " + postData['last_name'],
			email = postData['email'],
		)
		return user

	def user_remove(self, id):
		user = User.objects.get(id=id)
		user.delete()
		return self	
		
	def user_edit(self, postData, id):
		user = User.objects.get(id=id)
		user.name = postData['first_name']+" "+postData['last_name']
		user.email = postData['email']
		user.save()
		return self


class User(models.Model):
	name = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()

	def __unicode__(self):
		return "name: {}, email: {}, id: {}".format(self.name, self.email, self.id)

