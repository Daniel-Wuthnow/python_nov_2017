# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Item(models.Model):
	name = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=4,decimal_places=2)

	def __unicode__(self):
		return "name: {}, price: {}".format(self.name, self.price) 