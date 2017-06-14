from django.conf.urls import patterns, url
from django.views.generic import RedirectView

from . import views

urlpatterns = patterns(
    "",
    url(r"^objednavaci-list/$", views.manage_orders, name="objedn_list"),
)
