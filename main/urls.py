from django.conf import settings
from django.conf.urls import (
    patterns,
    url,
)
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

if settings.PRODUCTION:
    urlpatterns += patterns('', (r'^static/(.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}), )
