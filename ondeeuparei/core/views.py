# coding: utf-8
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as log_out
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.utils.translation import ugettext as _
from ondeeuparei.core.models import Reminder
from ondeeuparei.core.forms import ReminderForm



def login(request):
    return render(request, 'core/login.html')

def logout(request):
    log_out(request)
    return redirect('login')

@login_required()
def board(request):
    reminders = Reminder.objects.filter(user=request.user).order_by('title')
    return render(request, 'core/board.html', { 'reminders': reminders })

@login_required()
def create(request):
    if(request.method == 'POST'):
        return create_post(request)
    else:
        return render(request, 'core/create.html', {'form' : ReminderForm() })

@login_required()
def create_post(request):
    form = ReminderForm(request.POST)
    
    if not form.is_valid():
        return render(request, 'core/create.html', { 'form' : form })
    
    reminder = form.save(commit=False)
    reminder.user = request.user
    reminder.save()
    
    return HttpResponseRedirect(reverse('board'))

@login_required()
def remove(request, id_reminder):
    reminder = get_object_or_404(Reminder, pk=id_reminder)

    if reminder.user == request.user:
        reminder.delete()
        messages.success(request, _('Success! Your reminder was deleted.'))
    else:
        messages.error(request, _('You cant delete this reminder.'))

    return HttpResponseRedirect(reverse('board'))