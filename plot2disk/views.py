#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tempfile
import Gnuplot

from django.conf import settings

class Plot:
  def __init__(self, plot_conf):
    self.plot_conf = plot_conf

  def to_disk(self):
    # TODO: trouver un moyen joli pour spécifier, pour chaque format de sortie,
    # une extension et des options sympa
    # (ex. 'postscript' -> extension : '.ps', options : enhanced=1,color=1)
    c = self.plot_conf
    g = Gnuplot.Gnuplot(debug=0)
    g('set terminal unknow')
    # ajout de titre
    g.title(c['title'])
    g.xlabel(c['legend_x'])
    g.ylabel(c['legend_y'])
    # mise en place des données à partir de la chaine brute
    l = c['data'].split(u'\n')
    data = map ((lambda x: map(float,x.split(u' '))),l)
    # creation du graphe
    g.plot(Gnuplot.Data(data,with_=c['style'].encode()))
    # création d'un fichier temporaire
    temp = tempfile.NamedTemporaryFile(suffix='.'+c['out_format'], dir=settings.STATIC_PATH+'/plot/', delete=False)
    # copie du graphe dans le fichier
    g.hardcopy(temp.name, terminal=c['out_format'])
    return settings.STATIC_URL+'plot/' + temp.name[temp.name.rfind("/")+1:]
