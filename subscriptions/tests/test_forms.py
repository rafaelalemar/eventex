# coding: utf-8
from django.test import TestCase
from subscriptions.forms import SubscriptionForm

class SubscriptionFormTest(TestCase):
        def make_validated_form(self, **kwargs):
            data = dict(name='Rafael Vidal', email="rafaelalemar@gmail.com", cpf='134.176.861-99', phone="05163201254")
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

        def test_email_is_optimal(self):
            'Email is optimal'
            form = self.make_validated_form(email='')
            self.assertFalse(form.errors)

        def test_name_must_be_capitalizee(self):
            'Name must be capitalized'
            form = self.make_validated_form(name="RAFAEL Vidal")
            self.assertEqual('Rafael Vidal', form.cleaned_data['name'])

        def test_must_inform_email_or_phone(self):
            'Email and Phone are optional, but one must be informed.'
            form = self.make_validated_form(email='', phone='')
            self.assertItemsEqual(['__all__'], form.errors)