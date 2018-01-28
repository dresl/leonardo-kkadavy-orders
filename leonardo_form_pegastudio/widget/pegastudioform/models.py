# -#- coding: utf-8 -#-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from leonardo.module.web.models import Widget
from leonardo_form_pegastudio.models import PegastudioOrders


class PegastudioFormWidget(Widget):

    def get_items(self):
        return PegastudioOrders.objects.all().order_by("-datum")

    class Meta:
        abstract = True
        verbose_name = _('Pegastudio module')
        verbose_name_plural = _('Pegastudio modules')
