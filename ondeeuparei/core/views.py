# coding: utf-8
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as log_out
from ondeeuparei.core.models import Reminder

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
    return render(request, 'core/create.html')