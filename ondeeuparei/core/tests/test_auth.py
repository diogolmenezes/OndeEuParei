# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse

class TestAuth(TestCase):
    def setUp(self):
        self.response = self.client.get(reverse('auth'))

    def test_get(self):
        ''' url auth must exist '''
        self.assertEqual(200, self.response.status_code)

    def test_html(self):
        ''' auth html must have js to redirect to board and close popup '''
        self.assertContains(self.response, '<script')
        self.assertContains(self.response, 'parent.')
        self.assertContains(self.response, reverse('board'))
        self.assertContains(self.response, 'close()')
