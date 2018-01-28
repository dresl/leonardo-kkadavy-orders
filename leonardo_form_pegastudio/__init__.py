# -*- coding: utf-8 -*-
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

default_app_config = 'leonardo_form_pegastudio.Config'


class Default(object):

    optgroup = 'Pegastudio form widgets'

    apps = [
        'leonardo_form_pegastudio'
    ]

    widgets = [
        'leonardo_form_pegastudio.widget.pegastudioform.models.PegastudioFormWidget'
    ]
    config = {
        'ORDER_DEFAULT_TO_EMAIL':
        ('to@email.com', u"E-mail, na který se budou odesílat objednávky."),
        'COLOR_CHOICES':
        ('color choices',(('R', 'Red'),('B', 'Blue'),('G', 'Green'),
        ))
    }

    js_files = [
        'formset/jquery.formset.js'
    ]

    public = True


class Config(AppConfig, Default):
    name = 'leonardo_form_pegastudio'
    verbose_name = "Objednávky"


default = Default()
