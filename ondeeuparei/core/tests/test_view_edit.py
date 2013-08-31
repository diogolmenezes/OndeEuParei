# coding: utf-8
from django.test import TestCase
from ondeeuparei.core.models import Reminder
from django.core.urlresolvers import reverse

class TestViewEdit(TestCase):
    fixtures = ['test_user.json', 'test_reminder.json']

    def setUp(self):
        self.client.login(username='admin', password='admin')
        self.response = self.client.get(reverse('edit', kwargs={'id_reminder':1}))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)
