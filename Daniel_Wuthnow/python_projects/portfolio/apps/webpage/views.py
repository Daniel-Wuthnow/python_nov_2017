# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	return render(request, 'webpage/index.html')

def about(request):
	return render(request, 'webpage/about.html')

def contact(request):
	return render(request, 'webpage/contact.html')

def email(request):
    subject = request.subject
    message = request.message
    email_from = request.email
    recipient_list = ['003wuthnowd@gmail.com',]
    send_mail( subject, message, email_from, recipient_list, fail_silently=True )
    return redirect('/')