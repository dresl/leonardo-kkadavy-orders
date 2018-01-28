# encoding: utf-8
from django.contrib import admin
from django.conf import settings
from leonardo_form_pegastudio.models import PegastudioOrders, PegastudioProducts


class PegastudioProductsInline(admin.TabularInline):
    model = PegastudioProducts
    extra = 1


class PegastudioOrdersAdmin(admin.ModelAdmin):
    model = PegastudioOrders
    def get_readonly_fields(self, request, obj=None):
        if obj is None:
            return ['pub_date']
        else:
            return ['pub_date']
        return []
    inlines = [PegastudioProductsInline]
    list_display = ('prijmeni', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date','prijmeni']
    search_fields = ['prijmeni']

admin.site.register(PegastudioOrders, PegastudioOrdersAdmin)
