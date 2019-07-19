# -*- coding:utf-8 -*-

from .base import *
import os


DEBUG = True

DATABASS = {
            'default':{
                    'ENGINE': "django.db.backends.sqlite3",
                    'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
                }
        }
