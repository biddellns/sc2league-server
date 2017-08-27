from .base import *


DEBUG = False

ALLOWED_HOSTS = ['.' + os.environ['DOMAIN']]

# Extra security settings
CSRF_COOKIE_SECURE = True

SESSION_COOKIE_SECURE = True

X_FRAME_OPTIONS = 'DENY'
