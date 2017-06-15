# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.utils import timezone

from crispy_forms.layout import \
    HTML, Field, Layout, Fieldset, MultiField, Div, Submit, ButtonHolder
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import PrependedText
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.models import User
from django.contrib.auth.tokens import \
    default_token_generator as token_generator
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from horizon import messages
from horizon.utils import validators
from horizon_contrib.forms import SelfHandlingForm
from django.conf import settings
from django import forms
from django.forms import ModelForm, inlineformset_factory, BaseFormSet
from django.db import models
from django.forms import Field as DjangoField
from .models import KkadavyOrders, KkadavyProducts


DjangoField.default_error_messages = {
    'required': "Toto pole je povinné.",
    'invalid': "Zadejte správný formát e-mailu."
}


class KkadavyOrderForm(ModelForm):

    class Meta:
        model = KkadavyOrders
        exclude = ()

KkadavyOrderFormSet = inlineformset_factory(KkadavyOrders, KkadavyProducts,
                                            form=KkadavyOrderForm, extra=1)
