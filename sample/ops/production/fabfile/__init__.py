# -*- coding:utf8 -*-
from fabric.api import task, run, local, cd, hosts, env

import time

from oozappa.config import get_config
_settings = get_config()

from common.functions import _deploy_template_sample_a

test_host = ('192.168.0.10',) #FIXME

@task
def ls():
    u'''run ls command on local machine.'''
    local('ls -la')

@task
def ps():
    u'''run ls command on local machine.'''
    local('ps ax')

@task
def sleep():
    u'''sleep 5 second.'''
    print('stop 5 sec...')
    time.sleep(5)
    print('5 sec... passed')

@task
def printsetting():
    u'''print setting from staging.vars and common.vars'''
    print(_settings)

@task
@hosts(test_host)
def deploy_template_sample_a():
    _deploy_template_sample_a(_settings.sample_template_vars.sample_a)
