# -*- coding: utf-8 -*-
"""Application configuration.

Most configuration is set via environment variables.

For local development, use a .env file to set
environment variables.
"""
from environs import Env
import os
import timedelta
env = Env()
env.read_env()
path = os.path.abspath(os.path.dirname(__name__))
base_dir=os.path.abspath(os.path.dirname(__name__))
ENV = env.str('FLASK_ENV', default='production')
DEBUG = ENV == 'development'
SQLALCHEMY_DATABASE_URI = 'sqlite:///'+ os.path.join(base_dir,'dev_database.sqlite')
SECRET_KEY =  'sercet_key'
CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.
SQLALCHEMY_TRACK_MODIFICATIONS = False
WTF_CSRF_CHECK_DEFAULT=False
#session-setting
SESSION_PERMANENT=True
PERMANENT_SESSION_LIFETIME = timedelta.days=7
SESSION_TYPE='filesystem'
SESSION_FILE_DIR =  os.mkdir(os.path.join(path,'session'))if not os.path.exists(os.path.join(path,'session')) else os.path.join(path,'session')
SESSION_FILE_THRESHOLD = 1000
JSON_AS_ASCII = False

#./webpack/manifest.json
#WEBPACK_MANIFEST_PATH = 'None'
