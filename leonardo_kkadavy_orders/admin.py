# encoding: utf-8
from django.contrib import admin
from django.conf import settings
from leonardo_kkadavy_orders.models import KkadavyOrders, KkadavyProducts


class KkadavyProductInline(admin.TabularInline):
    model = KkadavyProducts
    extra = 1


class KkadavyOrdersAdmin(admin.ModelAdmin):
    model = KkadavyOrders
    def get_readonly_fields(self, request, obj=None):
        if obj is None:
            return ['pub_date']
        else:
            return ['pub_date']
        return []
    inlines = [KkadavyProductInline]
    list_display = ('prijmeni', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date','prijmeni']
    search_fields = ['prijmeni']

admin.site.register(KkadavyOrders, KkadavyOrdersAdmin)
