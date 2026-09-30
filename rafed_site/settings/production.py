import os
import dj_database_url
from .base import *

DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY', 'some-default-fallback-key-that-should-be-changed')
ALLOWED_HOSTS = ['*']

# Parse database configuration from $DATABASE_URL
db_from_env = dj_database_url.config(conn_max_age=600)
if db_from_env:
    DATABASES['default'].update(db_from_env)

# Insert WhiteNoise into MIDDLEWARE right after SecurityMiddleware
try:
    sec_idx = MIDDLEWARE.index('django.middleware.security.SecurityMiddleware')
    MIDDLEWARE.insert(sec_idx + 1, 'whitenoise.middleware.WhiteNoiseMiddleware')
except ValueError:
    MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

try:
    from .local import *
except ImportError:
    pass
