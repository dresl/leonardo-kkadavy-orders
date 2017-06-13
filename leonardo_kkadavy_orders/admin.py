# encoding: utf-8
from django.contrib import admin
from django.conf import settings
from leonardo_kkadavy_orders.models import KkadavyOrders, KkadavyProducts

class KkadavyProductInline(admin.TabularInline):
    model = KkadavyProducts
    extra = 1

class KkadavyOrdersAdmin(admin.ModelAdmin):
    model = KkadavyOrders
    inlines = [KkadavyProductInline]
    list_display = ('title', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date','title']
    search_fields = ['title']

admin.site.register(KkadavyOrders, KkadavyOrdersAdmin)
