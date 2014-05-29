# coding: utf-8
from django.test import TestCase
from subscriptions.models import Subscription

class DetailTest(TestCase):

    def setUp(self):
        s = Subscription.objects.create(
            name="Rafael Vidal",
            cpf="000000000012",
            email="outro@email.com",
            phone="47-91943004"
        )
        self.resp = self.client.get('/inscricao/%d/' % s.pk)

    def test_get(self):
        'GET /inscricao/1/ should return status 200'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Uses template'
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_detail.html')

    def test_context(self):
        'Context must have a subscription instance'
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        'Check if subscription data was rendered'
        self.assertContains(self.resp, 'Rafael Vidal')



    class DetailNotFound(TestCase):
        def Test_not_fount(self):
            response = self.client.get('/inscricao/0/')
            self.assertEqual(404, response.status_code)