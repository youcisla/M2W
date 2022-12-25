from django.shortcuts import render, redirect

# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import SignUpView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.conf import settings
from django.http import *


signin_page = 'registration/signin.html'
home_page = 'registration/home.html'

def signin(request):
    if request.method == "POST":
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return HttpResponseRedirect( settings.LOGIN_REDIRECT_URL )
    return render(request, signin_page)


def signout(request):
    logout(request)
    return redirect('/')




