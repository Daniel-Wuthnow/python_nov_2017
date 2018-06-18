# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserManager(models.Manager):

	def user_add(self, postData, fileData):
		user = User.objects.create(
			name = postData['name'],
			email = postData['email'],
			age = postData['age'],
			picture = fileData['picture'],
		)
		return user

	def user_remove(self, number):
		user = User.objects.get(id=number)
		user.delete()
		return self

	def user_edit(self, postData, fileData, number):
		user = User.objects.get(id=number)
		user.name = postData['name']
		user.email = postData['email']
		user.age = postData['age']
		user.picture = fileData['picture']
		user.save()
		return user

class User(models.Model):
	name = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	age = models.CharField(max_length=3)
	picture = models.ImageField(upload_to='images', blank=True)

	objects = UserManager()
# user once you have a better understanding on handling images
# picture = models.CharField(max_length=200)
