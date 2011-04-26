from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm

#env.hosts = ['cynddl@halfr.homedns.org:22']
env.hosts = ['ploter@ssh.alwaysdata.com:22']

def clear():
  local('rm *.pyc')
  local('rm */*.pyc')
  local('rm static/plot/*')

def test():
  local('./manage.py test plot2disk', capture=False)
  local('./manage.py test web', capture=False)

def pack():
  local('tar czf /tmp/my_project.tgz .', capture=False)

def prepare_deploy():
  test()
  pack()

def deploy():
  put('/tmp/my_project.tgz', '/tmp/')
  with cd('/home/ploter/ploter_prod'):
  #with cd('/srv/plot_er'):
    run('tar xzf /tmp/my_project.tgz')
    run('chmod 777 static/plot/')

def all():
  prepare_deploy()
  deploy()
