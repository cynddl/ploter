#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.template import RequestContext, loader
from web.models import PlotForm
from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
  t = loader.get_template('web/index.html')
  # création d'un formulaire pré-rempli
  form = PlotForm({'data':u'0 1\n1 2\n2 3\n3 4\n4 5'})
  c = RequestContext(request, {'form':form})
  return render_to_response('web/index.html', c)
