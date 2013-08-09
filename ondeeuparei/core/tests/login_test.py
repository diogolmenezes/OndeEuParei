from django.test import TestCase
from django.core.urlresolvers import reverse
from ondeeuparei import settings


class LoginTest(TestCase):
    fixtures = ['test_user.json']

    def setUp(self):
        self.response = self.client.get(reverse('login'))

    def test_get(self):
        """
        get / deve retornar 200
        """
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'core/login.html')

    def test_html(self):
        self.assertContains(self.response, '<html')
        self.assertContains(self.response, '<a', 1)
        self.assertContains(self.response, 'href="/login/facebook', 1)

    def test_login(self):
        self.client.login(username='admin', password='admin')
        response_board = self.client.get(reverse('board'))
        self.assertEqual(200, response_board.status_code)

    def test_logout(self):
        self.client.login(username='admin', password='admin')
        response_board = self.client.get(reverse('board'))
        self.assertEqual(200, response_board.status_code)
        self.client.get(reverse('logout'))
        response_board = self.client.get(reverse('board'))
        self.assertRedirects(response_board, settings.LOGIN_URL + '?next=' + reverse('board'))
