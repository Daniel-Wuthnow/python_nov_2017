# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import random
from time import gmtime, strftime
# Create your views here.
def index(request):
	if 'activities' not in request.session:
		request.session['activities'] = []
	if 'time' not in request.session:
		request.session['time'] = strftime("%Y-%m-%d %H:%M:%S %p", gmtime())
	if 'gold' not in request.session:
		request.session['gold'] = 0
	if 'farm' not in request.session:
		request.session['farm'] = 0
	if 'cave' not in request.session:
		request.session['cave'] = 0
	if 'house' not in request.session:
		request.session['house'] = 0
	if 'casino' not in request.session:
		request.session['casino'] = 0
	contex = {
		'activities': request.session['activities'],
		'gold': request.session['gold'],
		
	}
	return render(request, 'first_app/index.html', contex)

def process_money(request):
	if request.method == "POST":
		if request.POST['building'] == 'farm':
			request.session['time'] = strftime("%Y-%m-%d %H:%M:%S %p", gmtime())
			request.session['farm'] = random.randrange(10, 21)
			request.session['gold'] += request.session['farm']
			request.session['activities'].append("You earned {} from the farm! {}".format(request.session['farm'], request.session['time']))
		if request.POST['building'] == 'cave':
			request.session['time'] = strftime("%Y-%m-%d %H:%M:%S %p", gmtime())
			request.session['cave'] = random.randrange(5, 11)
			request.session['gold'] += request.session['cave']
			request.session['activities'].append("You earned {} from the cave! {}".format(request.session['cave'], request.session['time']))
		if request.POST['building'] == 'house':
			request.session['time'] = strftime("%Y-%m-%d %H:%M:%S %p", gmtime())
			request.session['house'] = random.randrange(2, 6)
			request.session['gold'] += request.session['house']
			request.session['activities'].append("You earned {} from the house! {}".format(request.session['house'], request.session['time']))
		if request.POST['building'] == 'casino':
			request.session['time'] = strftime("%Y-%m-%d %H:%M:%S %p", gmtime())
			request.session['casino'] = (random.randrange(0, 101)-50)
			if request.session['casino'] >= 0:
				request.session['gold'] += request.session['casino']
				request.session['activities'].append("You earned {} from the casino! {}".format(request.session['casino'], request.session['time']))
			elif request.session['casino'] < 0:
				request.session['gold'] += request.session['casino']
				request.session['activities'].append("You lost {} from the casino! {}".format(request.session['casino'], request.session['time']))

	return redirect('/')

def clear(request):
	request.session.clear()
	return redirect('/')