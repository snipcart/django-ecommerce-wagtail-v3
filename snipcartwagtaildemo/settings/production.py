from .base import *
import django_heroku

DEBUG = False

try:
    from .local import *
except ImportError:
    pass

django_heroku.settings(locals())