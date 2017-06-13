# encoding: utf-8
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _
from .widget import *

default_app_config = 'leonardo_kkadavy_orders.Config'

class Default(object):

    optgroup = 'Objednávky knedlíků'

    apps = [
        'leonardo_kkadavy_orders'
    ]

    widgets = [
        'leonardo_kkadavy_orders.widget.kkadavyorders.models.KkadavyOrdersWidget'
    ]

    public = True


class Config(AppConfig):
    name = 'leonardo_kkadavy_orders'
    verbose_name = "Objednávky knedlíků"


default = Default()
