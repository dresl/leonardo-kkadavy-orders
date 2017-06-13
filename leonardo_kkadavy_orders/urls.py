from django.conf.urls import patterns, url
from django.views.generic import RedirectView

from . import views

urlpatterns = patterns(
    "",
    url(r"^objednavaci-list/$", views.manage_articles, name="objedn_list"),
)
