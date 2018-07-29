from .settings import *
import os

# Disable debug
DEBUG = True

# Looks up secret in following order:
#  1. /run/secret/<key>
#  2. Environment variable named <key>
#  3. Value of default or None if no default supplied
def secret(key, default=None):
    root = os.environ.get('SECRETS_ROOT','/run/secrets')
    path = os.path.join(root,key)
    if os.path.isfile(path):
        with open(path) as f:
            return f.read().rstrip()
    else:
        return os.environ.get(key,default)

# Set secret key
SECRET_KEY = secret('SECRET_KEY', SECRET_KEY)

# Must be explicitly specified when Debug is disabled
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(',')

# Database settings
DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': os.environ.get('MYSQL_DATABASE','todobackend'),
        'USER': os.environ.get('MYSQL_USER','todo'),
        'PASSWORD': secret('MYSQL_PASSWORD','password'),
        'HOST': os.environ.get('MYSQL_HOST','localhost'),
        'PORT': os.environ.get('MYSQL_PORT','3306'),
    },
    'OPTIONS': {
      'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
    }
}

STATIC_ROOT = os.environ.get('STATIC_ROOT', '/public/static')
MEDIA_ROOT = os.environ.get('MEDIA_ROOT', '/public/media')