# coding: utf-8
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^inscricao/', include('subscriptions.urls', namespace='subscriptions')), ## Aponta para Subscriptions
    url(r'^admin/', include(admin.site.urls)), ## URL da página de ADMIN

    # Este tem que ficar no final, caso contrário não vai achar os outros acima
    url(r'', include('core.urls', namespace='core')),                         ## Aponta para o core.urls

)
