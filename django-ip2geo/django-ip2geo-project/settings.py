
# Django settings for debate project.
# http://docs.djangoproject.com/en/dev/ref/settings/

import os
ROOT_PATH = os.path.dirname(__file__)

PROJECTNAME = 'django-ip2geo-project'

try:
    from local_settings import *
except ImportError:
    pass

DEBUG = True

############################################################################
# PRODUCTION
if not DEBUG:
  TEMPLATE_STRING_IF_INVALID = ''
  TEMPLATE_DEBUG = DEBUG

############################################################################
# DEVELOPMENT
else:
  TEMPLATE_STRING_IF_INVALID = ''
  TEMPLATE_DEBUG = DEBUG

  DATABASE_ENGINE = 'sqlite3'
  DATABASE_NAME = ROOT_PATH + '/database.sqlite3'

############################################################################

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'b-ptn5@ey-qk28at=yc01*wl1r+-*ii6iri8fqch((9^p0&f4n'

TEMPLATE_CONTEXT_PROCESSORS = (
    'ip2geo.context_processors.add_session',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'ip2geo.middleware.CityMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    ROOT_PATH + '/templates',
    MEDIA_ROOT,
)

INSTALLED_APPS = (
    'django.contrib.sessions',
    'ip2geo',
)

