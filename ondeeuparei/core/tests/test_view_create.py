# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse
from ondeeuparei import settings


class TestViewCreate(TestCase):

    fixtures = ['test_user.json'] # this fixture contains user admin.

    def setUp(self):
        self.client.login(username='admin', password='admin')
        self.response = self.client.get(reverse('create'))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'core/create.html')