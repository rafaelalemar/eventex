# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r
from core.models import Speaker


class SpeakerDetailTest(TestCase):

    def setUp(self):
        Speaker.objects.create(
            name="Rafael Alemar",
            slug="rafael-alemar",
            url="https://plus.google.com/u/0/108549132187205263216/posts",
            description='Passionate software developer!'
        )
        url = r('core:speaker_detail', kwargs={'slug': 'rafael-alemar'})
        self.resp = self.client.get(url)

    def test_get(self):
        'GET should result in 200'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Template should be core/speaker_detail.html'
        self.assertTemplateUsed(self.resp, 'core/speaker_detail.html')

    def test_context(self):
        'Speaker must be in a context'
        speaker = self.resp.context['speaker']
        self.assertIsInstance(speaker, Speaker)



class SpeakerDetailFoun(TestCase):

    def test_not_found(self):
        url = r('core:speaker_detail', kwargs={'slug': 'john-doe'})
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)