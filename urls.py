from django.conf.urls.defaults import *
from plot_er import settings

from django.contrib import admin
admin.autodiscover()

from dajaxice.core import dajaxice_autodiscover
dajaxice_autodiscover()


urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    # serve static files
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_PATH}),
    # web frontend
    (r'^$', 'web.views.index'),
    # dajaxice urls
    (r'^%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls')),
    (r'^sentry/', include('sentry.urls')),
)
