# encoding: utf-8

from django.db import models
from django.utils.translation import ugettext_lazy as _
from leonardo.module.web.models import Widget
from leonardo_kkadavy_orders.models import KkadavyOrders


class KkadavyOrdersWidget(Widget):

    def get_items(self):
        return KkadavyOrders.objects.all().order_by("-datum")

    class Meta:
        abstract = True
        verbose_name = _('Order kkadavy')
        verbose_name_plural = _('Orders kkadavy')
