# coding: utf-8
from django.test import TestCase
from django.contrib.auth.models import User
from django.db import IntegrityError
from model_mommy import mommy
from ondeeuparei.core.models import Reminder

class TestModelBoard(TestCase):
    def test_user_is_required(self):
        reminder = Reminder(title='dexter', place='123')
        self.assertRaises(IntegrityError, reminder.save)

    def test_title_is_required(self):
        user = mommy.make(User)
        reminder = Reminder(title=None, place='123', user=user)
        self.assertRaises(IntegrityError, reminder.save)

    def test_place_is_required(self):
        user = mommy.make(User)
        reminder = Reminder(title='dexter', place=None, user=user)
        self.assertRaises(IntegrityError, reminder.save)