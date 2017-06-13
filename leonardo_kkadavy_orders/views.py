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
from leonardo import forms, messages

from .forms import KkadavyOrderForm
from django.forms import formset_factory

def manage_articles(request):
    KkadavyOrderFormSet = formset_factory(KkadavyOrderForm)
    if request.method == 'POST':
        formset = KkadavyOrderFormSet(request.POST, request.FILES)
        if formset.is_valid():
            # do something with the formset.cleaned_data
            pass
    else:
        formset = KkadavyOrderFormSet()
    return render(request, 'kkadavy_orders/manage.html', {'formset': formset})