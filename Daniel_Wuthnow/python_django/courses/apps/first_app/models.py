# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class CourseManager(models.Manager):
	def course_valadation(self, postData):
		errors = []
		if len(postData['name'])<5:
			errors.append('You need a longer name')
		if len(postData['desc'])<15:
			errors.append('There needs to be a longer description')
		return errors

	def course_add(self, postData):
		course = Course.objects.create(
			name = postData['name'],
			desc = postData['desc'],
		)
		return course

	def course_delete(self, number):
		course = Course.objects.get(id=number)
		course.delete()
		return self

class Course(models.Model):
	name = models.CharField(max_length=200)
	desc = models.CharField(max_length=200)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = CourseManager()

	def __unicode__(self):
		return "name: {}, desc: {}, id: {}".format(self.name, self.desc, self.id)


class CommentManager(models.Manager):
	def comment_add(self, postData, number):
		course = Course.objects.get(id=number)
		comment = Comment.objects.create(
			comment = postData['comment'],
			course = course,
		)
		return comment

	def comment_valadation(self, postData):
		errors = []
		if len(postData['comment']) == 0:
			errors.append('You need to have a comment')
		return errors

	def comment_delete(self, number):
		comment = Comment.objects.get(id=number)
		comment.delete()
		return self

class Comment(models.Model):
	comment = models.CharField(max_length=200)
	course = models.ForeignKey(Course, related_name="comment")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = CommentManager()

	def __unicode__(self):
		return "comment: {}, course: {}, id: {}".format(self.comment, self.course, self.id)
