# coding: utf-8
from django.test import TestCase
from core.models import Contact, Speaker, Talk

class ContactManagerTest(TestCase):

    def setUp(self):
        s = Speaker.objects.create(name='Henrique Bastos',
                                   slug='henrique-bastos', url='http://henriquebastos.net')

        s.contact_set.add(
            Contact(kind='E', value='henrique@bastos.net'),
            Contact(kind='P', value='47 9194-3004'),
            Contact(kind='F', value='47 3313-1212')
        )

    def test_emails(self):
        qs = Contact.emails.all()
        expected = ['<Contact: henrique@bastos.net>']
        self.assertQuerysetEqual(qs, expected)

    def test_phones(self):
        qs = Contact.phones.all()
        expected = ['<Contact: 47 9194-3004>']
        self.assertQuerysetEqual(qs, expected)

    def test_faxes(self):
        qs = Contact.faxes.all()
        expected = ['<Contact: 47 3313-1212>']
        self.assertQuerysetEqual(qs, expected)



class PeriodManagerTest(TestCase):

    def setUp(self):
        Talk.objects.create(title='Morning Talk', start_time='10:00')
        Talk.objects.create(title='Afternoon Talk', start_time='12:00')

    def test_morning(self):
        'Should return only talks before 12:00'
        self.assertQuerysetEqual(Talk.objects.at_morning(), ['Morning Talk'], lambda t: t.title)

    def test_afternoon(self):
        'Should return only talks starting on 12:00'
        self.assertQuerysetEqual(Talk.objects.at_afternoon(), ['Afternoon Talk'], lambda t: t.title)