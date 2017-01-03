from django.conf.urls import include, url
from django.views.generic import TemplateView

import views


urlpatterns = [
    #url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^$', views.index, name='home'),
    url(r'^redirect/$', views.token_exchange, name='token_exchange'),
    url(r'^home/$', views.userhome, name='userhome'),

    url(r'', include('social.apps.django_app.urls', namespace='social')),
]
