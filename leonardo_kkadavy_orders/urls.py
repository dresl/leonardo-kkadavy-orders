from django.conf.urls import patterns, url
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    url(r'objednavaci-list/pridat/$', views.KkadavyOrderCreate.as_view(), name='objedn_list'),
]
