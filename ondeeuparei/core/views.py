# coding: utf-8
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as log_out

def login(request):
    return render(request, 'core/login.html')

def logout(request):
    log_out(request)
    return redirect('login')

@login_required()
def board(request):
    return render(request, 'core/board.html')