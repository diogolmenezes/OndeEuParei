# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse
from ondeeuparei.core.forms import ReminderForm

class TestFormBoard(TestCase):
    fixtures = ['test_user.json'] # this fixture contains user admin.
    def setUp(self):
        self.client.login(username='admin', password='admin')
        self.resp = self.client.get(reverse('create'))
        self.form = self.resp.context['form']

    def test_has_fields(self):
        self.assertItemsEqual(['title', 'place'], self.form.fields)