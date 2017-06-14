# encoding: utf-8
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
import datetime


CHOICES_TYPE_KNEDLIKY = (
 ('HOUSKOVÉ KNEDLÍKY', (
   ('khouskovy300', 'Knedlík houskový 300g'),
   ('khouskovy600', 'Knedlík houskový 600g'),
   ('khouskovy800', 'Knedlík houskový 800g'),
   ('kstarocesky', 'Staročeský knedlík 600g'),
   ('kvyberovy', 'Výběrový knedlík 500g'),
  )
 ),
 ('OVOCNÉ KNEDLÍKY', (
   ('kpb', 'Kynuté knedlíky plněné ovocem – borůvka 350g'),
   ('kpj', 'Kynuté knedlík plněné ovocem – jahoda 350g'),
   ('kpm', 'Kynuté knedlík plněné ovocem – meruňka 350g'),
   ('tps', 'Tvarohové knedlíky plněné ovocem – švestka 350g'),
   ('tpj', 'Tvarohové knedlíky plněné ovocem – jahoda 350g'),
   ('tpm', 'Tvarohové knedlíky plněné ovocem – meruňka 350g'),
  )
 ),
 ('BRAMBOROVÉ KNEDLÍKY', (
   ('bpu', 'Bramborové knedlíky plněné uzeninou 350g'),
   ('bpum', 'Bramborové knedlíky plněné uzeným masem 350g'),
   ('b2pum', 'Bramborové knedlíky 2x plněné uzeným masem 350g'),
   ('bpp', 'Bramborové taštičky plněné povidly 350g'),
   ('ptpt', 'Bramborové taštičky plněné tvarohem 350g'),
   ('bk', 'Bramborový knedlík 400g'),
   ('bs', 'Bramborové špalíčky 400g'),
   ('bsm', 'Bramborové šišky s mákem 400g'),

  )
 ),
 ('OSTATNÍ VÝROBKY', (
   ('chk', 'Chlupaté knedlíky 400g'),
   ('hom', 'Halušky od Marušky 400g'),
   ('bp', 'Babiččiny palačinky 300g'),
   ('b', 'Bramboráky 400g'),
   ('lt', 'Listové těsto 500g'),
  )
 ),
)

class KkadavyOrders(models.Model):
    jmeno = models.CharField(max_length=255, verbose_name="Jméno", default='')
    prijmeni = models.CharField(
        max_length=255, verbose_name="Příjmení", default='')
    email = models.EmailField(verbose_name="E-mail", default='')
    telefon = models.PositiveIntegerField(
        verbose_name="Telefon", default="")
    pub_date = models.DateTimeField('Datum Objednavky', auto_now_add=True)
    def __unicode__(self):
        return self.prijmeni
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=2) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    class Meta:
        ordering = ['prijmeni', ]
        verbose_name = 'Objednavka'
        verbose_name_plural = 'Objednavky'


class KkadavyProducts(models.Model):
    order = models.ForeignKey(KkadavyOrders,verbose_name="Objednavka", related_name="orderproduct_set")
    type_of_product = models.CharField(verbose_name="Produkt", choices=CHOICES_TYPE_KNEDLIKY, max_length=100)
    quantity = models.PositiveIntegerField(verbose_name="Počet")
    def __unicode__(self):
        return self.type_of_product

    class Meta:
        ordering = ['type_of_product', ]
        verbose_name = 'Produkt'
        verbose_name_plural = 'Produkty'
