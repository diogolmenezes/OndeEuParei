# coding: utf-8
from django import forms
from django.utils.translation import ugettext as _
from ondeeuparei.core.models import Reminder

class ReminderForm(forms.ModelForm):
    title = forms.CharField(label=_("Title"), max_length=20)
    place = forms.CharField(label=_("Place"), max_length=7)

    class Meta:
        model  = Reminder
        fields = ('title', 'place')