# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.

# class UsersManager(models.Manager):
# 	def create(self, form_data):
		


class Users(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	age = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return "first_name: {}, last_name: {}, email: {}, age: {}, created at: {}, updated at: {}".format(self.first_name, self.last_name, self.email, self.age, self.created_at, self.updated_at)

