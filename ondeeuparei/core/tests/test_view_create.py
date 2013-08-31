# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from model_mommy import mommy
from ondeeuparei import settings
from ondeeuparei.core.models import Reminder
from ondeeuparei.core.forms import ReminderForm

class TestViewCreate(TestCase):

    fixtures = ['test_user.json'] # this fixture contains user admin.

    def setUp(self):
        self.client.login(username='admin', password='admin')
        self.response = self.client.get(reverse('create'))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'core/form.html')

    def test_context(self):
        form = self.response.context['form']
        self.assertIsInstance(form, ReminderForm)

    def test_html(self):
        self.assertContains(self.response, '<form action="%s" method="post"' % reverse('create'), 1)
        self.assertContains(self.response, '<input', 4)
        self.assertContains(self.response, 'type="text"', 2)
        self.assertContains(self.response, 'type="submit', 1)
        self.assertContains(self.response, 'csrfmiddlewaretoken', 1)
        self.assertContains(self.response, 'href="%s"' % reverse('board'), 1)


class TestValidCreatePost(TestCase):
    fixtures = ['test_user.json']
    def setUp(self):
        self.client.login(username='admin', password='admin')
        data = dict(title='dexter', place='S08E04', user=mommy.make(User))
        self.response = self.client.post(reverse('create'), data, follow=True)

    def test_save(self):
        ''' valid post must save reminder '''
        self.assertTrue(Reminder.objects.exists())


    def test_redirect(self):
        ''' valid post must redirect '''
        self.assertRedirects(self.response, reverse('board'))


class TestInvalidCreatePost(TestCase):
    fixtures = ['test_user.json']
    def setUp(self):
        self.client.login(username='admin', password='admin')
        data = dict(title='', place='')
        self.response = self.client.post(reverse('create'), data)

    def test_has_errors(self):
        ''' invalid post must have erros '''
        self.assertTrue(self.response.context['form'].errors)

    def test_dont_redirect(self):
        ''' invalid posts must not redirect '''
        self.assertEqual(200, self.response.status_code)

    def test_dont_save(self):
        ''' invalid post dont save '''
        self.assertFalse(Reminder.objects.exists())
