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
		if len(form_data['name']) < 3:
			errors.append('Name required.')
		if len(form_data['username']) < 3:
			errors.append('Username required.')
		if len(form_data['password']) < 8:
			errors.append('Password should have more than 8 characters.')
		if form_data['password'] != form_data['confirm_password']:
				errors.append('Password should match.')	
		duplicate = User.objects.filter(username = form_data['username'])
		if len(duplicate) == 1:
			errors.append('Username taken.')
		return errors


	def register(self, form_data):
		pw = str(form_data['password'])
		hashed_pw = bcrypt.hashpw(pw,bcrypt.gensalt())

		user = User.objects.create(
			name = form_data['name'],
			username = form_data['username'],
			password = hashed_pw,
		)
		return user

	def login_validation(self, form_data):
		errors= []
		user = User.objects.filter(username=form_data['username']).first()
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
		user = User.objects.filter(username=form_data['username']).first()
		return user


	def trip_validation(self, form_data):
		errors = []
		if len(form_data['destination']) == 0:
			errors.append('Need a Destination.')
		if len(form_data['plan']) == 0:
			errors.append('Need a Plan.')
		start_date = form_data['start_date']
		end_date = form_data['end_date']
		if start_date > end_date:
			errors.append('End date can not come before the start date.')
		return errors

	def add_trip(self, form_data):

		trip = Trip.objects.create(
			destination = form_data['destination'],
			start_date = form_data['start_date'],
			end_date = form_data['end_date'],
			plan = form_data['plan']
		)
		return trip


class User (models.Model):
	name = models.CharField(max_length=255)
	username = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateField()
	updated_at = models.DateField()
	objects = UserManager()

	def __unicode__(self):
		return "name: {}, username: {}, password: {}, id: {}".format(self.name, self.username, self.password, self.id)

class Trip (models.Model):
	destination = models.CharField(max_length=255)
	start_date = models.DateField()
	end_date = models.DateField()
	plan = models.CharField(max_length=255)
	User = models.ManyToManyField(User, related_name="Trip")
	objects = UserManager()

	def __unicode__(self):
		return "destination: {}, start_date: {}, end_date: {},plan: {}, id: {} ".format(self.destination, self.start_date, self.end_date,self.plan, self.id)