from django.shortcuts import render,HttpResponse, redirect
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
	response = "Hello, I am your first request!"
	return render(request, 'first_app/index.html')