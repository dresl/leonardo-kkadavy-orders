# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KkadavyOrders',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('jmeno', models.CharField(default=b'', max_length=255, verbose_name='Jm\xe9no')),
                ('prijmeni', models.CharField(default=b'', max_length=255, verbose_name='P\u0159\xedjmen\xed')),
                ('email', models.EmailField(default=b'', max_length=254, verbose_name='E-mail')),
                ('telefon', models.PositiveIntegerField(default=b'', verbose_name='Telefon')),
                ('adresa', models.CharField(default=b'', max_length=255, verbose_name='Doru\u010dovac\xed adresa')),
                ('firma', models.CharField(default=b'', help_text=b'Nepovinn\xc3\xa9 pole', max_length=255, verbose_name='N\xe1zev firmy', blank=True)),
                ('ico', models.CharField(default=b'', help_text='Nepovinn\xe9 pole', max_length=255, verbose_name='I\u010cO', blank=True)),
                ('dic', models.CharField(default=b'', help_text='Nepovinn\xe9 pole', max_length=255, verbose_name='DI\u010c', blank=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Datum objedn\xe1vky')),
            ],
            options={
                'ordering': ['prijmeni'],
                'verbose_name': 'Objedn\xe1vka',
                'verbose_name_plural': 'Objedn\xe1vky',
            },
        ),
        migrations.CreateModel(
            name='KkadavyProducts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_of_product', models.CharField(max_length=100, verbose_name='Produkt', choices=[(b'HOUSKOV\xc3\x89 KNEDL\xc3\x8dKY', ((b'khouskovy300', b'Knedl\xc3\xadk houskov\xc3\xbd 300g'), (b'khouskovy600', b'Knedl\xc3\xadk houskov\xc3\xbd 600g'), (b'khouskovy800', b'Knedl\xc3\xadk houskov\xc3\xbd 800g'), (b'kstarocesky', b'Staro\xc4\x8desk\xc3\xbd knedl\xc3\xadk 600g'), (b'kvyberovy', b'V\xc3\xbdb\xc4\x9brov\xc3\xbd knedl\xc3\xadk 500g'))), (b'OVOCN\xc3\x89 KNEDL\xc3\x8dKY', ((b'kpb', b'Kynut\xc3\xa9 knedl\xc3\xadky pln\xc4\x9bn\xc3\xa9 ovocem \xe2\x80\x93 bor\xc5\xafvka 350g'), (b'kpj', b'Kynut\xc3\xa9 knedl\xc3\xadky pln\xc4\x9bn\xc3\xa9 ovocem \xe2\x80\x93 jahoda 350g'), (b'kpm', b'Kynut\xc3\xa9 knedl\xc3\xadky pln\xc4\x9bn\xc3\xa9 ovocem \xe2\x80\x93 meru\xc5\x88ka 350g'), (b'tps', b'Tvarohov\xc3\xa9 knedl\xc3\xadky pln\xc4\x9bn\xc3\xa9 ovocem \xe2\x80\x93 \xc5\xa1vestka 350g'), (b'tpj', b'Tvarohov\xc3\xa9 knedl\xc3\xadky pln\xc4\x9bn\xc3\xa9 ovocem \xe2\x80\x93 jahoda 350g'), (b'tpm', b'Tvarohov\xc3\xa9 knedl\xc3\xadky pln\xc4\x9bn\xc3\xa9 ovocem \xe2\x80\x93 meru\xc5\x88ka 350g'))), (b'BRAMBOROV\xc3\x89 KNEDL\xc3\x8dKY', ((b'bpu', b'Bramborov\xc3\xa9 knedl\xc3\xadky pln\xc4\x9bn\xc3\xa9 uzeninou 350g'), (b'bpum', b'Bramborov\xc3\xa9 knedl\xc3\xadky pln\xc4\x9bn\xc3\xa9 uzen\xc3\xbdm masem 350g'), (b'b2pum', b'Bramborov\xc3\xa9 knedl\xc3\xadky 2x pln\xc4\x9bn\xc3\xa9 uzen\xc3\xbdm masem 350g'), (b'bpp', b'Bramborov\xc3\xa9 ta\xc5\xa1ti\xc4\x8dky pln\xc4\x9bn\xc3\xa9 povidly 350g'), (b'ptpt', b'Bramborov\xc3\xa9 ta\xc5\xa1ti\xc4\x8dky pln\xc4\x9bn\xc3\xa9 tvarohem 350g'), (b'bk', b'Bramborov\xc3\xbd knedl\xc3\xadk 400g'), (b'bs', b'Bramborov\xc3\xa9 \xc5\xa1pal\xc3\xad\xc4\x8dky 400g'), (b'bsm', b'Bramborov\xc3\xa9 \xc5\xa1i\xc5\xa1ky s m\xc3\xa1kem 400g'))), (b'OSTATN\xc3\x8d V\xc3\x9dROBKY', ((b'chk', b'Chlupat\xc3\xa9 knedl\xc3\xadky 400g'), (b'hom', b'Halu\xc5\xa1ky od Maru\xc5\xa1ky 400g'), (b'bp', b'Babi\xc4\x8d\xc4\x8diny pala\xc4\x8dinky 300g'), (b'b', b'Brambor\xc3\xa1ky 400g'), (b'lt', b'Listov\xc3\xa9 t\xc4\x9bsto 500g')))])),
                ('quantity', models.PositiveIntegerField(verbose_name='Po\u010det')),
                ('order', models.ForeignKey(related_name='orderproduct_set', verbose_name='Objedn\xe1vka', to='leonardo_kkadavy_orders.KkadavyOrders')),
            ],
            options={
                'ordering': ['type_of_product'],
                'verbose_name': 'Produkt',
                'verbose_name_plural': 'Produkty',
            },
        ),
    ]
