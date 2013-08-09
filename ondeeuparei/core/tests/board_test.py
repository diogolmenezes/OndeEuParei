# coding: #utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse
from ondeeuparei import settings

class BoardWithoutLoginTest(TestCase):

    def test_login_required(self):
        response = self.client.get(reverse('board'))
        self.assertRedirects(response, settings.LOGIN_URL + '?next=' + reverse('board') )

class BoardLoginTest(TestCase):
    fixtures = ['test_user.json']

    def setUp(self):
        self.client.login(username='admin', password='admin')
        self.response = self.client.get(reverse('board'))

    def test_is_logged_in(self):
        self.assertEqual(200, self.response.status_code)

    def test_html(self):
        self.assertContains(self.response, 'href="' + reverse('logout') + '"')