from django.core.exceptions import ValidationError
from django.test import TestCase
from core.models import Speaker, Contact



class SpeakerModelTest(TestCase):

    def setUp(self):
        self.speaker = Speaker(name='Rafael Alemar',
                               slug='rafael-alemar',
                               url='https://plus.google.com/u/0/108549132187205263216/posts',
                               description='Passionate software developer')
        self.speaker.save()

    def test_create(self):
        'Speaker instance should be saved'
        self.assertEqual(1, self.speaker.pk)

    def test_unicode(self):
        'Speaker string representation should be the name'
        self.assertEqual(u'Rafael Alemar', unicode(self.speaker))



class ContactModelTest(TestCase):

    def setUp(self):
        self.speaker =Speaker.objects.create(
            name='Rafael Alemar',
            slug='rafael-alemar',
            url='https://plus.google.com/u/0/108549132187205263216/posts',
            description='Passionate software developer'
        )

    def test_email(self):
        contact = Contact.objects.create(speaker=self.speaker, kind='E', value='rafaelalemar@gmail.com')
        self.assertEqual(1, contact.pk)

    def test_phone(self):
        contact = Contact.objects.create(speaker=self.speaker, kind='P', value='47-91943004')
        self.assertEqual(1, contact.pk)

    def test_fax(self):
        contact = Contact.objects.create(speaker=self.speaker, kind='F', value='47-33051042')
        self.assertEqual(1, contact.pk)

    def test_kind(self):
        'Contact kind should be limited to E, P or E'
        contact = Contact(speaker=self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_unicode(self):
        'Contact string representation should be value'
        contact = Contact(speaker=self.speaker, kind='E', value='rafaelalemar@gmail.com')
        self.assertEqual(u'rafaelalemar@gmail.com', unicode(contact))