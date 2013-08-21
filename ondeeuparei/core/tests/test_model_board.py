# coding: utf-8
from django.test import TestCase
from django.contrib.auth.models import User
from django.db import IntegrityError
from model_mommy import mommy
from ondeeuparei.core.models import Reminder

class TestModelBoard(TestCase):
    def test_user_is_required(self):
        """ user is required """
        reminder = Reminder(title='dexter', place='123')
        self.assertRaises(IntegrityError, reminder.save)

    def test_title_is_required(self):
        """ title is required """
        user = mommy.make(User)
        reminder = Reminder(title=None, place='123', user=user)
        self.assertRaises(IntegrityError, reminder.save)

    def test_place_is_required(self):
        """ place is required """
        user = mommy.make(User)
        reminder = Reminder(title='dexter', place=None, user=user)
        self.assertRaises(IntegrityError, reminder.save)

    def test_date_must_be_today(self):
        """ on save, date must be today """
        import datetime
        user = mommy.make(User)
        reminder = Reminder(title='dexter', place='123', user=user)
        reminder.save()
        self.assertEqual(reminder.date, datetime.date.today())
        