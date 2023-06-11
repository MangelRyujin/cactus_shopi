from .base import *
import dj_database_url

DEBUG = 'RENDER' not in os.environ

ALLOWED_HOSTS = []

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:    
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.squlite3',    
        conn_max_age=600    
    )
}

STATIC_URL = 'static/'

if not DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'