# encoding: utf-8

from django.db import models
from django.utils.translation import ugettext_lazy as _
from leonardo.module.web.models import Widget
from leonardo_kkadavy_orders.models import KkadavyOrders, KkadavyProducts
from django.forms import inlineformset_factory


class KkadavyOrdersWidget(Widget):

    def get_items(self):
        return KkadavyOrders.objects.all().order_by("-pub_date")

    class Meta:
        abstract = True
        verbose_name = 'Order kkadavy'
        verbose_name_plural = 'Orders kkadavy'
