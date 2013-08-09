# coding: #utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse
from ondeeuparei import settings

class BoardTest(TestCase):
    fixtures = ['test_user.json']

    def test_login_required(self):
        response = self.client.get(reverse('board'))
        self.assertRedirects(response, settings.LOGIN_URL + '?next=' + reverse('board') )
        self.client.login(username='admin', password='admin')
        #self.client.login(username='admin', password='pbkdf2_sha256$10000$0sidbMHmHZTi$AxxuJYA2RKSkZoCh9ZiBQJqsqukn5jkhszu5eQx8z0g=')
        response = self.client.get(reverse('board'))
        self.assertEqual(200, response.status_code)