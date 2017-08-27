from .base import *
import os

DEBUG = False


base_domain = '.' + os.environ['DOMAIN']
ALLOWED_HOSTS = [base_domain,]

# Extra security settings
CSRF_COOKIE_SECURE = True

SESSION_COOKIE_SECURE = True

X_FRAME_OPTIONS = 'DENY'
