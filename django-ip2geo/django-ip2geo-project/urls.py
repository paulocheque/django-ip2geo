from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
)

if settings.DEBUG:
    urlpatterns += patterns('',
    # Media
    (r'^'+ settings.MEDIA_URL[1:] + '(?P<path>.*)$', 
     'django.views.static.serve', 
     {'document_root': settings.MEDIA_ROOT }),
    )