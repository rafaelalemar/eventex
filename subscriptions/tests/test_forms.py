# coding: utf-8
from django.test import TestCase
from subscriptions.forms import SubscriptionForm

class SubscriptionFormTest(TestCase):
        def make_validated_form(self, **kwargs):
            data = dict(name='Rafael Vidal', email="rafaelalemar@gmail.com", cpf='12345678901', phone="05163201254")
            data.update(kwargs)
            form = SubscriptionForm(data)
            form.is_valid()
            return form


        def test_form_has_fields(self):
            'Form must have 4 fields.'
            form = SubscriptionForm()
            self.assertItemsEqual(['name', 'email', 'cpf', 'phone'], form.fields)

        def test_cpf_is_digit(self):
            'CPF must only accept digit'
            form = self.make_validated_form(cpf="ABCD5678901")
            self.assertItemsEqual(['cpf'], form.errors)

        def test_cpf_has_11_digits(self):
            'CPF must contain 11 digits'
            form = self.make_validated_form(cpf="1234")
            
            self.assertItemsEqual(['cpf'], form.errors)