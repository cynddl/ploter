from plot2disk.views import Plot
from web.models import PlotForm

from django.conf import settings

from dajax.core import Dajax
from dajaxice.core import dajaxice_functions

import commands

def test(request, form):
  form = PlotForm(form)
  dajax = Dajax()
  if form.is_valid():
    dajax.remove_css_class('#form input,select','error-field')
    my_plot = Plot(form.cleaned_data)
    filename = my_plot.to_disk()
    dajax.assign('#image', 'src', filename)
  else:
    dajax.remove_css_class('#form input,select','error-field')
    for error in form.errors:
      dajax.add_css_class('#id_%s' % error,'error-field')
  return dajax.json()

def upload(request, form):
  form = PlotForm(form)
  dajax = Dajax()
  if form.is_valid():
    dajax.remove_css_class('#form input,select','error-field')
    my_plot = Plot(form.cleaned_data)
    filename = my_plot.to_disk()
    url = commands.getoutput(settings.UIMGE_PATH + " --ig " + settings.PROJECT_PATH + filename)
    dajax.assign('#image', 'src', url)
  else:
    dajax.remove_css_class('#form input,select','error-field')
    for error in form.errors:
      dajax.add_css_class('#id_%s' % error,'error-field')
  return dajax.json()
 

dajaxice_functions.register(test)
dajaxice_functions.register(upload)
