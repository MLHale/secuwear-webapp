# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from .forms import *

# Create your views here.
def temperature_list(request):
	data = Temperature.objects.all()
	return render(request, 'temperature_list.html', {'data': data})

def temperature_new(request):
	if request.method == 'POST':
		form = TemperatureForm(request.POST)
		#print form
		
		if form.is_valid():
			temperature = form.save(commit=False)
			time = form.cleaned_data['time']
			celsius = form.cleaned_data['celsius']
			print time
			temperature.save()



			return HttpResponseRedirect('/temperature_list')
	else:
		form = TemperatureForm()
		
	return render(request, 'temperature_edit.html', {'form': form})
   
