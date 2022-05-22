from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.contrib import messages
from .forms import UserRegisterForm

from templates.forms import SignUpForm
from .models import Customers
from django.core.exceptions import *


def index(request):
    return render(request, 'form.html')


def search(request):
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
        try:
            user = Customers.objects.get(name=search_id)
            # do something with user
            html = ("<H1>%s</H1>", user)
            return HttpResponse(html)
        except Customers.DoesNotExist:
            return HttpResponse("no such user")
    else:
        return render(request, 'form.html')


def home_view(request):
    return render(request, 'home.html')


def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.profile.first_name = form.cleaned_data.get('first_name')
        user.profile.last_name = form.cleaned_data.get('last_name')
        user.profile.email = form.cleaned_data.get('email')
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'form.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'usr/register.html', {'form': form})
