#!/usr/bin/python
# -*- coding: utf8 -*-


from django.db import models

choice_style = [
    ('lines','Lignes'),
    ('points','Points'),
    ('linespoints', 'Points et lignes'),
    ('impulses', 'Lignes verticales'),
    ('boxes', 'Histogramme')
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
  style = models.CharField(max_length=300,choices=choice_style)
  legend_x = models.CharField(max_length=300, blank=True)
  legend_y = models.CharField(max_length=300, blank=True)
  #color = models.CharField(max_length=30,choices=choice_color)

  def __str__(self):
    return self.title
