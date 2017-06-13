# encoding: utf-8
from django.db import models
from django.conf import settings
from django.utils import timezone


class KkadavyOrders(models.Model):
    title = models.CharField(max_length=200, verbose_name="Název objednávky")
    pub_date = models.DateTimeField('Datum objednávky')
    def __unicode__(self):
        return self.title
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=2) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    class Meta:
        ordering = ['title', ]
        verbose_name = 'Objednávka'
        verbose_name_plural = 'Objednavky'


class KkadavyProducts(models.Model):
    order = models.ForeignKey(KkadavyOrders,verbose_name="Objednávka")
    type_of_product = models.CharField(verbose_name="Produkt", max_length=100, default='Den: ')
    amount = models.PositiveIntegerField(verbose_name="Množství", default=None)
    quantity = models.PositiveIntegerField(verbose_name='Počet')
    def __unicode__(self):
        return self.type_of_product

    class Meta:
        ordering = ['type_of_product', ]
        verbose_name = 'Produkt'
        verbose_name_plural = 'Produkty'
