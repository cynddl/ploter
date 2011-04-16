#!/usr/bin/python
# -*- coding: utf8 -*-

from django.forms import ModelForm,Textarea

from plot2disk.models import PlotModel

class PlotForm(ModelForm):
  class Meta:
    model = PlotModel
    widgets = {
        'data': Textarea(attrs={'cols':80, 'rows':15})
    }
