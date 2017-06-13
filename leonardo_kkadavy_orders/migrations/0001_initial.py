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
                ('jmeno', models.CharField(default=b'', max_length=255, verbose_name=b'Jm\xc3\xa9no')),
                ('prijmeni', models.CharField(default=b'', max_length=255, verbose_name=b'P\xc5\x99\xc3\xadjmen\xc3\xad')),
                ('email', models.EmailField(default=b'', max_length=254, verbose_name=b'E-mail')),
                ('telefon', models.PositiveIntegerField(default=0, verbose_name=b'Telefon')),
                ('pub_date', models.DateTimeField(verbose_name=b'Datum objedn\xc3\xa1vky')),
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
                ('type_of_product', models.CharField(max_length=100, verbose_name=b'Produkt', choices=[(b'HOUSKOV\xc3\x89 KNEDL\xc3\x8dKY', ((b'khouskovy', b'Knedl\xc3\xadk houskov\xc3\xbd 300g'), (b'khouskovy', b'Knedl\xc3\xadk houskov\xc3\xbd 600g'), (b'khouskovy', b'Knedl\xc3\xadk houskov\xc3\xbd 800g'), (b'kstarocesky', b'Staro\xc4\x8desk\xc3\xbd knedl\xc3\xadk 600g'), (b'kvyberovy', b'V\xc3\xbdb\xc4\x9brov\xc3\xbd knedl\xc3\xadk 500g'))), (b'OVOCN\xc3\x89 KNEDL\xc3\x8dKY', ((b'vhs', b'Kynut\xc3\xa9 knedl\xc3\xadky pln\xc4\x9bn\xc3\xa9 ovocem \xe2\x80\x93 bor\xc5\xafvka 350g'), (b'dvd', b'Kynut\xc3\xa9 knedl\xc3\xadk pln\xc4\x9bn\xc3\xa9 ovocem \xe2\x80\x93 jahoda 350g'), (b'dvd', b'Kynut\xc3\xa9 knedl\xc3\xadk pln\xc4\x9bn\xc3\xa9 ovocem \xe2\x80\x93 meru\xc5\x88ka 350g'), (b'dvd', b'Tvarohov\xc3\xa9 knedl\xc3\xadky pln\xc4\x9bn\xc3\xa9 ovocem \xe2\x80\x93 \xc5\xa1vestka 350g'), (b'dvd', b'Tvarohov\xc3\xa9 knedl\xc3\xadky pln\xc4\x9bn\xc3\xa9 ovocem \xe2\x80\x93 jahoda 350g'), (b'dvd', b'Tvarohov\xc3\xa9 knedl\xc3\xadky pln\xc4\x9bn\xc3\xa9 ovocem \xe2\x80\x93 meru\xc5\x88ka 350g'))), (b'BRAMBOROV\xc3\x89 KNEDL\xc3\x8dKY', ((b'vhs', b'Bramborov\xc3\xa9 knedl\xc3\xadky pln\xc4\x9bn\xc3\xa9 uzeninou 350g'), (b'vhs', b'Bramborov\xc3\xa9 knedl\xc3\xadky pln\xc4\x9bn\xc3\xa9 uzen\xc3\xbdm masem 350g'), (b'vhs', b'Bramborov\xc3\xa9 knedl\xc3\xadky 2x pln\xc4\x9bn\xc3\xa9 uzen\xc3\xbdm masem 350g'), (b'vhs', b'Bramborov\xc3\xa9 ta\xc5\xa1ti\xc4\x8dky pln\xc4\x9bn\xc3\xa9 povidly 350g'), (b'vhs', b'Bramborov\xc3\xa9 ta\xc5\xa1ti\xc4\x8dky pln\xc4\x9bn\xc3\xa9 tvarohem 350g'), (b'vhs', b'Bramborov\xc3\xbd knedl\xc3\xadk 400g'), (b'vhs', b'Bramborov\xc3\xa9 \xc5\xa1pal\xc3\xad\xc4\x8dky 400g'), (b'vhs', b'Bramborov\xc3\xa9 \xc5\xa1i\xc5\xa1ky s m\xc3\xa1kem 400g'))), (b'OSTATN\xc3\x8d V\xc3\x9dROBKY', ((b'vhs', b'Chlupat\xc3\xa9 knedl\xc3\xadky 400g'), (b'vhs', b'Halu\xc5\xa1ky od Maru\xc5\xa1ky 400g'), (b'vhs', b'Babi\xc4\x8d\xc4\x8diny pala\xc4\x8dinky 300g'), (b'vhs', b'Brambor\xc3\xa1ky 400g'), (b'vhs', b'Listov\xc3\xa9 t\xc4\x9bsto 500g')))])),
                ('quantity', models.PositiveIntegerField(verbose_name=b'Po\xc4\x8det')),
                ('order', models.ForeignKey(verbose_name=b'Objedn\xc3\xa1vka', to='leonardo_kkadavy_orders.KkadavyOrders')),
            ],
            options={
                'ordering': ['type_of_product'],
                'verbose_name': 'Produkt',
                'verbose_name_plural': 'Produkty',
            },
        ),
    ]
