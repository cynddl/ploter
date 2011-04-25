#!/usr/bin/python
# -*- coding: utf8 -*-


from django.db import models

choice_style = [
  ('lines', 'Lines'),
  ('points', 'Points'),
  ('linespoints', 'Points and lines'),
  ('impulses', 'Vertical lines'),
  ('boxes', 'Histogram')
  ]

# Not every format supported by gnuplot is suitable for web use (e.g.`latex').
# A nice feature would be, for formats other than png/jpf/gif, to provide only a link
# to the generated file!
# The output formats supported by the gnuplot bindings are listed in `termdef.py'
choice_format = [
  ('png', 'png'),
  # ('gif', 'gif'), # not available in Gnuplot.py
  # ('jpeg', 'jpeg'), # not available in Gnuplot.py
  ('svg', 'svg')
  ]

#choice_color = [
#    (1, u'rouge'),
#    (2, u'vert'),
#    (3, u'bleu'),
#    (4, u'violet'),
#    (5, u'cyan'),
#    (6, u'marron'),
#    (7, u'orange clair'),
#    (8, u'orange foncé')
#    ]


class PlotModel(models.Model):
  title = models.CharField(max_length=300, blank=True)
  data = models.CharField(max_length=3000)
  style = models.CharField(max_length=300, choices=choice_style)
  legend_x = models.CharField(max_length=300, blank=True)
  legend_y = models.CharField(max_length=300, blank=True)
  out_format = models.CharField(max_length=50, choices=choice_format)
  #color = models.CharField(max_length=30,choices=choice_color)

  def __str__(self):
    return self.title
