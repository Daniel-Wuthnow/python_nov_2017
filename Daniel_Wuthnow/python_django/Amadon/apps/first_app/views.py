# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Item

# Create your views here.
def index(request):
	contex = {
		'shirts' : Item.objects.get(id=1),
		'sweater' : Item.objects.get(id=2),
		'cup' : Item.objects.get(id=3),
		'book' : Item.objects.get(id=4),
	}
	return render(request, "first_app/index.html", contex)

def checkout(request):
	contex = {
		'shirts' : Item.objects.get(id=1),
		'sweater' : Item.objects.get(id=2),
		'cup' : Item.objects.get(id=3),
		'book' : Item.objects.get(id=4),
		'amount' : request.session['amount'],
	}
	return render(request, "first_app/checkout.html", contex)

def add(request):
	if 'amount' not in request.session:
		request.session['amount'] = 0
	request.session['amount'] += int(request.POST['quantity'])

	if 'total' not in request.session:
		request.session['total'] = 0
	request.session['total'] = int(request.POST['quantity']) * float(request.POST['action'])

	if 'sum' not in request.session:
		request.session['sum'] = 0
	request.session['sum'] += request.session['total']
	return redirect('/Amadon/checkout')

def clear(request):
	request.session.clear()
	return redirect('/Amadon')

def back(request):
	del request.session['total']
	return redirect('/Amadon')