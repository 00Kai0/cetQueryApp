"""
WSGI config for cetQueryApp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

'''
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cetQueryApp.settings")

application = get_wsgi_application()
'''

import os
from os.path import join,dirname,abspath
 
PROJECT_DIR = dirname(dirname(abspath(__file__)))
import sys 
sys.path.insert(0,PROJECT_DIR) 
 
os.environ["DJANGO_SETTINGS_MODULE"] = "cetQueryApp.settings" # 7
 
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
