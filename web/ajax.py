from plot2disk.views import Plot
from web.models import PlotForm

from dajax.core import Dajax
from dajaxice.core import dajaxice_functions

import uimge

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
  u = uimge.Uimge()
  u.set_host(uimge.Hosts.s_smages)
  if form.is_valid():
    dajax.remove_css_class('#form input,select','error-field')
    my_plot = Plot(form.cleaned_data)
    filename = my_plot.to_disk()
    u.upload(filename)
    print u.get_urls()
    dajax.assign('#image', 'src', u.get_urls()[0])
  else:
    dajax.remove_css_class('#form input,select','error-field')
    for error in form.errors:
      dajax.add_css_class('#id_%s' % error,'error-field')
    return dajax.json()
 

dajaxice_functions.register(test)
