from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.views.generic import RedirectView

from hello.views import AboutView, create_model


urlpatterns = patterns('',
                       url(r'^$', AboutView.as_view(), name='index'),
						url(r'^create_post/$', create_model),
						(r'^favicon\.ico$', RedirectView.as_view(url='/static/img/favicon.ico/')),)