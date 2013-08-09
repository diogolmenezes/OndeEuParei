"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class LoginTest(TestCase):
    def test_get(self):
        """
        get / deve retornar 200
        """
        self.response = self.client.get('/')
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.response = self.client.get('/')
        self.assertTemplateUsed(self.response, 'core/login.html')

    def test_html(self):
        self.response = self.client.get('/')
        self.assertContains(self.response, '<html')
        self.assertContains(self.response, '<a', 1)
        self.assertContains(self.response, 'href="/login/facebook', 1)


