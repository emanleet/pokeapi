# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from pokemon import urls as pokemon_urls
from pokemon_v2 import urls as pokemon_v2_urls

# need to make sure v2 urls resolve last so angular routes have control
# v2 = [ url(r'^', include(pokemon_v2_urls)) ]

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),

    url(r'^media/(?P<path>.*)',
        'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),

    url(r'^static/(?P<path>.*)',
        'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT}),

    url(r'^$', 'config.views.home'),

    url(r'^docs/$', 
        TemplateView.as_view(template_name='docs.html'),
        name="documentation"
    ),

    url(r'^docs2/$', 
        TemplateView.as_view(template_name='docs2.html'),
        name="documentation_v2"
    ),

    url(r'^about/$', 'config.views.about'),

    url(r'^', include(pokemon_urls)),
    
    url(r'^', include(pokemon_v2_urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # + v2