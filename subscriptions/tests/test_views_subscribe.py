from django.test import TestCase
from subscriptions.forms import SubscriptionForm
from subscriptions.models import Subscription
from django.core.urlresolvers import reverse as r


class SubscribeTest(TestCase):

    def setUp(self):
        self.resp = self.client.get(r('subscriptions:subscribe'))


    def test_get(self):
        'GET /inscricao/ mus return status 200'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Respnse should be a renderend template'
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    def test_html(self):
        'Html must contain input controls.'
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 5)
        self.assertContains(self.resp, 'type="text"', 3)
        self.assertContains(self.resp, 'type="email"')
        self.assertContains(self.resp, 'type="submit"')

    def test_csrf(self):
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        'Context must have the subscription form'
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)



class SubscribePostTest(TestCase):

    def setUp(self):
        data = dict(name="Rafael Vidal", cpf="824.086.610-72",  email="rafaelalemar@gmail.com", phone="47-91943004")
        self.resp = self.client.post(r('subscriptions:subscribe'), data)

    def test_post(self):
        'Valid POST should redirect to /inscricao/1/'
        self.assertEqual(302, self.resp.status_code)

    def test_save(self):
        'Valid POST must be saved'
        self.assertTrue(Subscription.objects.exists())


class SubscribeInvalidPostTest(TestCase):

    def setUp(self):
        data = dict(
            name="Rafael Vidal",
            cpf="000000000012",
            email="outro@email.com",
            phone="47-91943004"
        )
        self.resp = self.client.post(r('subscriptions:subscribe'), data)

    def test_post(self):
        'Invalid POST should not redirect'
        self.assertEqual(200, self.resp.status_code)

    def test_form_erros(self):
        'Form must contain errors'
        self.assertTrue(self.resp.context['form'].errors)

    def test_dont_save(self):
        'Do not save data'
        self.assertFalse(Subscription.objects.exists())



class TemplateRegressionTest(TestCase):
    def test_template_has_non_field_errors(self):
        'Check if non_field_errors are shown in template.'
        invalid_data = dict(name='Henrique Bastos', cpf='12345678901')
        response = self.client.post(r('subscriptions:subscribe'), invalid_data)
        self.assertContains(response, '<div class="alert alert-danger alert-dismissable alert-link">')