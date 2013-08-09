# coding: utf-8
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'core/login.html')

@login_required()
def board(request):
    return render(request, 'core/board.html')