# -*- coding: utf-8 -*-
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

try:
    from local_settings import APPS
except ImportError:
    pass

default_app_config = 'leonardo_kkadavy_orders.Config'


class Default(object):
    if 'leonardo_kkadavy_orders' in APPS:
        optgroup = 'Kkadavy widgets'

        apps = [
            'leonardo_kkadavy_orders'
        ]

        widgets = [
            'leonardo_kkadavy_orders.widget.kkadavyorders.models.KkadavyOrdersWidget'
        ]
        config = {
            'ORDER_DEFAULT_TO_EMAIL':
            ('to@email.com', u"E-mail, na který se budou odesílat objednávky."),
        }

        js_files = [
            'formset/jquery.formset.js'
        ]

        public = True


class Config(AppConfig, Default):
    name = 'leonardo_kkadavy_orders'
    verbose_name = u"Objednávky knedlíků"


default = Default()
