# coding: utf-8
from django import forms
from django.utils.translation import ugettext as _
from django.core.exceptions import ValidationError
from subscriptions.models import Subscription
from localflavor.br.forms import BRCPFField


def CPFValidator(value):
    if not value.isdigit():
        raise ValidationError(_(u'CPF deve conter apenas números'))

    if len(value) != 11:
        raise ValidationError(_(u'CPF deve conter 11 números'))


class SubscriptionForm(forms.ModelForm):
    cpf = BRCPFField(label=_('CPF'))

    class Meta:
        model = Subscription
        exclude = ('paid', )

    def __init__(self, *args, **kargs):
        super(SubscriptionForm, self).__init__(*args, **kargs)

        #self.fields['cpf'].validators.append(CPFValidator)

    def clean_name(self):
        name = self.cleaned_data['name']
        words = map(lambda w: w.capitalize(), name.split())
        capitalized_name = ' '.join(words)
        return capitalized_name

    def clean(self):
        super(SubscriptionForm, self).clean()

        if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
            raise ValidationError(_(u'Informe seu e-mail ou telefone'))

        return self.cleaned_data