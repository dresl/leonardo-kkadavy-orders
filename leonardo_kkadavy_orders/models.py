# encoding: utf-8
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
import datetime

CHOICES_TYPE_KNEDLIKY = (
 ('HOUSKOVÉ KNEDLÍKY', (
   ('khouskovy800', 'Knedlík houskový - velký 800g'),
   ('khouskovy800kr', 'Knedlík houskový - velký krájený 800g'),
   ('khouskovy600', 'Knedlík houskový - malý 600g'),
   ('khouskovy600kr', 'Knedlík houskový - malý krájený 600g'),
   ('khouskovy300', 'Knedlík houskový - mini 300g'),
   ('kstarocesky', 'Staročeský knedlík - 600g'),
   ('kstaroceskyk', 'Staročeský knedlík - krájený 600g'),
  )
 ),
 ('KYNUTÉ KNEDLÍKY', (
   ('kpb', 'Kynuté knedlíky plněné ovocem – borůvka 350g v bal. 4ks'),
   ('kpb1', 'Kynuté knedlíky plněné ovocem – borůvka v bal. 1ks (1 knedlík)'),
   ('kpj', 'Kynuté knedlíky plněné ovocem – jahoda 350g v bal. 4ks'),
   ('kpj1', 'Kynuté knedlíky plněné ovocem – jahoda v bal. 1ks (1 knedlík)'),
   ('kpm', 'Kynuté knedlíky plněné ovocem – meruňka 350g v bal. 4ks'),
   ('kpm1', 'Kynuté knedlíky plněné ovocem – meruňka v bal. 1ks (1 knedlík)'),
   ('ksnb', 'Kynuté knedlíky s náplní – borůvka 350g v bal. 6ks'),
   ('ksnb1', 'Kynuté knedlíky s náplní – borůvka v bal. 1ks (1 knedlík)'),
   ('ksnj', 'Kynuté knedlíky s náplní – jahoda 350g v bal. 6ks'),
   ('ksnj1', 'Kynuté knedlíky s náplní – jahoda v bal. 1ks (1 knedlík)'),
   ('ksnm', 'Kynuté knedlíky s náplní – meruňka 350g v bal. 6ks'),
   ('ksnm1', 'Kynuté knedlíky s náplní – meruňka v bal. 1ks (1 knedlík)'),
  )
 ),
 ('TVAROHOVÉ KNEDLÍKY', (
   ('tps', 'Tvarohové knedlíky plněné ovocem – švestka 350g v bal. 6ks'),
   ('tps1', 'Tvarohové knedlíky plněné ovocem – švestka v bal. 1ks (1 knedlík)'),
   ('tpj', 'Tvarohové knedlíky plněné ovocem – jahoda 350g v bal. 6ks'),
   ('tpj1', 'Tvarohové knedlíky plněné ovocem – jahoda v bal. 1ks (1 knedlík)'),
   ('tpm', 'Tvarohové knedlíky plněné ovocem – meruňka 350g v bal. 6ks'),
   ('tpm1', 'Tvarohové knedlíky plněné ovocem – meruňka v bal. 1ks (1 knedlík)'),
  )
 ),
 ('BRAMBOROVÉ KNEDLÍKY', (
   ('bpum', 'Bramborové knedlíky plněné uzeným masem - 350g v bal. 6ks'),
   ('bpum1', 'Bramborové knedlíky plněné uzeným masem - v bal. 1ks'),
   ('b2pum', 'Bramborové knedlíky 2x plněné uzeným masem - 350g v bal. 6ks'),
   ('b2pum1', 'Bramborové knedlíky 2x plněné uzeným masem - v bal. 1ks'),
   ('bkss', 'Bramborové knedlíky se švestkami - 500g v bal. 8ks'),
   ('bkss1', 'Bramborové knedlíky se švestkami - v bal. 1ks'),
   ('bpp', 'Bramborové taštičky plněné povidly - 350g v bal. 6ks'),
   ('bpp1', 'Bramborové taštičky plněné povidly - v bal. 1ks'),
   ('ptpt', 'Bramborové taštičky plněné tvarohem - 350g v bal. 6ks'),
   ('ptpt1', 'Bramborové taštičky plněné tvarohem - v bal. 1ks'),
   ('bk', 'Bramborový knedlík - 400g'),
   ('bkk', 'Bramborový knedlík - krájený 400g'),
   ('bs', 'Bramborové špalíčky - 400g'),
   ('bskg', 'Bramborové špalíčky - 1kg'),
   ('bsm', 'Bramborové šišky s mákem - 400g'),
   ('bsmkg', 'Bramborové šišky s mákem - 1kg'),
  )
 ),
 ('OSTATNÍ VÝROBKY', (
   ('chk', 'Chlupaté knedlíky - 400g'),
   ('chkkg', 'Chlupaté knedlíky - 1kg'),
   ('hom', 'Halušky od Marušky - 400g'),
   ('homkg', 'Halušky od Marušky - 1kg'),
   ('bp', 'Babiččiny palačinky - 300g v bal. 3ks'),
   ('bp1', 'Babiččiny palačinky - 1ks'),
   ('b', 'Bramboráky - 400g v bal. 5ks'),
   ('b1', 'Bramboráky - 1ks'),
   ('lt', 'Listové těsto - 500g'),
   ('ltkg', 'Listové těsto - 1kg'),
   ('kkarlovarsky', 'Karlovarský knedlík (při objednávce nad 15ks) - 500g'),
  )
 ),
)


class KkadavyOrders(models.Model):
    jmeno = models.CharField(max_length=255, verbose_name=u"Jméno", default='')
    prijmeni = models.CharField(
        max_length=255, verbose_name=u"Příjmení", default='')
    email = models.EmailField(verbose_name=u"E-mail", default='')
    telefon = models.PositiveIntegerField(verbose_name=u"Telefon", default="")
    adresa = models.CharField(max_length=255, verbose_name=u"Doručovací adresa", default='')
    firma = models.CharField(max_length=255, verbose_name=u"Název firmy", default='', blank=True, help_text="Nepovinné pole")
    ico = models.CharField(max_length=255, verbose_name=u"IČO", default='', blank=True, help_text=u"Nepovinné pole")
    dic = models.CharField(max_length=255, verbose_name=u"DIČ", default='', blank=True, help_text=u"Nepovinné pole")
    pub_date = models.DateTimeField(u'Datum objednávky', auto_now_add=True)
    def __unicode__(self):
        return (self.prijmeni + self.jmeno)
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=2) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = u'Nedávno vytvořené? (2 dny)'

    class Meta:
        ordering = ['prijmeni', ]
        verbose_name = u'Objednávka'
        verbose_name_plural = u'Objednávky'


class KkadavyProducts(models.Model):
    order = models.ForeignKey(KkadavyOrders,verbose_name=u"Objednávka", related_name="orderproduct_set")
    type_of_product = models.CharField(verbose_name=u"Produkt", choices=CHOICES_TYPE_KNEDLIKY, max_length=100)
    quantity = models.PositiveIntegerField(verbose_name=u"Počet")
    def __unicode__(self):
        return self.type_of_product

    class Meta:
        ordering = ['type_of_product', ]
        verbose_name = u'Produkt'
        verbose_name_plural = u'Produkty'
