# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse

class TestAuth(TestCase):
    def setUp(self):
        self.response = self.client.get(reverse('auth'))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_html(self):
        self.assertContains(self.response, '<script')
        self.assertContains(self.response, 'parent.')
        self.assertContains(self.response, reverse('board'))
        self.assertContains(self.response, 'close()')
