from django.conf.urls import url
from personal_app.views import AboutView, create_model


urlpatterns = [
                       url(r'^$', AboutView.as_view(), name='index'),
                       url(r'^create_post/$', create_model),
    ]
