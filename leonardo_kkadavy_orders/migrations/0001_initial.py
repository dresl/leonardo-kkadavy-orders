# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KkadavyOrders',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name=b'N\xc3\xa1zev objedn\xc3\xa1vky')),
                ('pub_date', models.DateTimeField(verbose_name=b'Datum objedn\xc3\xa1vky')),
            ],
        ),
        migrations.CreateModel(
            name='KkadavyProducts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_of_product', models.CharField(default=b'Den: ', max_length=100, verbose_name=b'Produkt')),
                ('amount', models.PositiveIntegerField(default=None, verbose_name=b'Mno\xc5\xbestv\xc3\xad')),
                ('quantity', models.PositiveIntegerField(verbose_name=b'Po\xc4\x8det')),
                ('order', models.ForeignKey(verbose_name=b'Objedn\xc3\xa1vka', to='leonardo_kkadavy_orders.KkadavyOrders')),
            ],
        ),
    ]
