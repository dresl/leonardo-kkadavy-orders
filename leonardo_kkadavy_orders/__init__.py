# -*- coding: utf-8 -*-
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

default_app_config = 'leonardo_kkadavy_orders.Config'


class Default(object):

    optgroup = 'Kkadavy widgets'

    apps = [
        'leonardo_kkadavy_orders'
    ]

    widgets = [
        'leonardo_kkadavy_orders.widget.kkadavyorders.models.KkadavyOrdersWidget'
    ]

    public = True


class Config(AppConfig, Default):
    name = 'leonardo_kkadavy_orders'
    verbose_name = "Objednavky knedliku"


default = Default()
