# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.auth import logout as auth_logout
from django.contrib.sites.models import Site
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.shortcuts import render
from leonardo.decorators import require_auth
from django.db import transaction
from leonardo import forms, messages
from django.core.urlresolvers import reverse_lazy
from django.forms import inlineformset_factory
from .models import KkadavyOrders, KkadavyProducts
from .forms import KkadavyOrderFormSet
from django.views.generic import CreateView
from leonardo.utils.emails import send_templated_email as send_mail


class KkadavyOrderCreate(forms.ModalFormView, forms.views.CreateView):
    model = KkadavyOrders
    template_name = "leonardo_kkadavy_orders/kkadavyorders_form.html"
    submit_label = "Objednat"

    def get_context_data(self, **kwargs):
        ret = super(KkadavyOrderCreate, self).get_context_data(**kwargs)

        if self.request.POST:
            ret['orderproducts'] = KkadavyOrderFormSet(self.request.POST)
        else:
            ret['orderproducts'] = KkadavyOrderFormSet()

        ret.update({
        	"view_name": "Objednavaci list",
        	"modal_size": 'lg',
            "modal_header": 'Objednávací list',
        	})
        return ret

    def form_valid(self, form):
        context = self.get_context_data()
        orderproducts = context['orderproducts']
        with transaction.atomic():
            self.object = form.save()
            if orderproducts.is_valid():
                orderproducts.instance = self.object
                orderproducts.save()
                prijmeni_text = orderproducts.data['prijmeni']
                subject = u"Objednávka - " + prijmeni_text
                send_mail(
                    subject,
                    'leonardo_kkadavy_orders/kkadavy_email.html',
                    {'jmeno': orderproducts.data['jmeno'],
                     'prijmeni': orderproducts.data['prijmeni'],
                     'telefon': orderproducts.data['telefon'],
                     'email': orderproducts.data['email'],
                     'adresa': orderproducts.data['adresa'],
                     'firma': orderproducts.data['firma'],
                     'ico': orderproducts.data['ico'],
                     'dic': orderproducts.data['dic'],
                     'order': KkadavyOrders.objects.get(id=orderproducts.instance.id,),
                    },
                    [email.strip() for email in settings.ORDER_DEFAULT_TO_EMAIL.split(',')],
                    fail_silently=False,
                )

        return super(KkadavyOrderCreate, self).form_valid(form)

