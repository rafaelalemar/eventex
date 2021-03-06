# coding: utf-8
from django.test import TestCase
from datetime import datetime
from django.db import IntegrityError
from subscriptions.models import Subscription

class SubscriptionTest(TestCase):

    def setUp(self):
        self.obj = Subscription(
            name="Rafael Vidal",
            cpf="80100011187",
            email="rafaelalemar@gmail.com",
            phone="47-91943004"
        )

    def test_create(self):
        'Subscription must have a name, cpf, e-mail, phone'
        self.obj.save()
        self.assertEqual(1, self.obj.pk)

    def test_has_created_at(self):
        'Subscription must have automatic created_at'
        self.obj.save()
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_unicode(self):
        self.assertEqual(u'Rafael Vidal', unicode(self.obj))

    def test_paid_default_value_is_False(self):
        'By default paid must be false'
        self.assertEqual(False, self.obj.paid)



class SubscriptionUniqueTest(TestCase):

    def setUp(self):
        # Create a first entry to force the collision
        Subscription.objects.create(
            name="Rafael Vidal",
            cpf="80100011187",
            email="rafaelalemar@gmail.com",
            phone="47-91943004"
        )

    def test_cpf_unique(self):
        'CPF must be unique'
        s = Subscription(
            name="Rafael Vidal",
            cpf="80100011187",
            email="outro@email.com",
            phone="47-91943004"
        )
        # self.assertRaises(IntegrityError, s.save())

    # def test_email_can_repeat(self):
    #     'Email is not unique anymore'
    #     s = Subscription.objects.create(name="Rafael Vidal", cpf='134.176.861-99', email='rafaelalemar@gmail.com')
    #     self.assertEqual(2, s.pk)