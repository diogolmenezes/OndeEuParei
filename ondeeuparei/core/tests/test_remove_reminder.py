from django.contrib.auth.models import User
from django.test import TestCase
from django.core.urlresolvers import reverse
from ondeeuparei.core.models import Reminder

class TestRemoveReminder(TestCase):

    fixtures = ['test_user.json'] # this fixture contains user admin.

    def setUp(self):
        user = User.objects.get(username='admin')
        Reminder.objects.create(title='dexter', place='S08E04', user=user)
        self.client.login(username='admin', password='admin')
        self.response = self.client.get(reverse('remove', kwargs={'id_reminder':1}), follow=True)

    def test_remove(self):
        ''' if is the owner od reminder, should can remove it  '''
        self.assertFalse(Reminder.objects.exists())

    def test_redirect_on_remove(self):
        '''must redirect after remove '''
        self.assertRedirects(self.response, reverse('board'))

    def test_show_message_on_remove(self):
        ''' must show message on delete '''
        self.assertContains(self.response, 'reminder was deleted')

class TestInvalidRemove(TestCase):

    fixtures = ['test_user.json'] # this fixture contains user admin.

    def setUp(self):
        user = User.objects.get(username='admin')
        Reminder.objects.create(title='dexter', place='S08E04', user=user)
        self.client.login(username='diogolmenezes', password='admin')
        self.response = self.client.get(reverse('remove', kwargs={'id_reminder':1}), follow=True)

    def test_dont_exclude_if_not_owner(self):
        ''' must cant remove if its not owner '''
        self.assertTrue(Reminder.objects.exists())

    def test_redirect_on_dont_remove(self):
        '''must redirect after dont remove '''
        self.assertRedirects(self.response, reverse('board'))

    def test_show_message_on_dont_remove(self):
        ''' must show message when dont remove '''
        self.assertContains(self.response, 'You cant delete this reminder.')