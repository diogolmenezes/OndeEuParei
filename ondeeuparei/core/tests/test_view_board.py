# coding: #utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from ondeeuparei import settings
from ondeeuparei.core.models import Reminder
import datetime

class TestViewBoardNoLogin(TestCase):

    def test_login_required(self):
        response = self.client.get(reverse('board'))
        self.assertRedirects(response, settings.LOGIN_URL + '?next=' + reverse('board'))

class TextViewBoardWithLogin(TestCase):

    fixtures = ['test_user.json'] # this fixture contains user admin.

    def setUp(self):
        user = User.objects.get(username='admin')
        Reminder.objects.create(title='dexter', place='S08E04', user=user)
        self.client.login(username='admin', password='admin')
        self.response = self.client.get(reverse('board'))

    def test_must_be_logged_in(self):
        self.assertEquals(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'core/board.html')

    def test_html(self):
        self.assertContains(self.response, 'href="' + reverse('logout') + '"')
        self.assertContains(self.response, 'href="%s"' % reverse('create'), 1)
        self.assertContains(self.response, '<ul class="reminder-list"', 1)
        self.assertContains(self.response, 'dexter')
        self.assertContains(self.response, 'S08E04')
        self.assertContains(self.response, datetime.date.today().strftime('%d-%m-%Y'))
        self.assertContains(self.response, reverse('remove', kwargs={'id_reminder':1}))

    def test_context(self):
        queryset = self.response.context['reminders']
        self.assertEquals(queryset.model, Reminder)
        self.assertEqual(1, queryset.count())