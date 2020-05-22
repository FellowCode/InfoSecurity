import urllib

from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import *
from django.contrib import auth
from django.conf import settings
from django.db.models import Q
import re
from urllib.parse import unquote
import json
from utils.shortcuts import iredirect
from utils.decorators import graphic_key as gr_key_decorator


def login(request):
    if request.user.is_authenticated:
        return redirect(reverse('main:index'))
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            auth.login(request, form.cleaned_data['user'])
            p = urllib.parse.urlencode(request.GET)
            return redirect(reverse('accounts:graphic_key') + '?' + p)
        return render(request, 'Accounts/Login.html', {'form': form})
    form = LoginForm()
    return render(request, 'Accounts/Login.html', {'form': form})


def graphic_key(request):
    if not request.user.is_authenticated:
        return redirect(reverse('accounts:login'))
    status = request.GET.get('status')
    if request.method == 'POST':
        gr_key = request.POST.get('gr_key')
        if status == 'new':
            request.session['graphic_key'] = gr_key
            return iredirect('accounts:graphic_key', get={'status': 'confirm'})
        elif status == 'confirm':
            if request.session['graphic_key'] == gr_key:
                request.user.gr_key = gr_key
                request.session['graphic_key'] = True
                request.user.save()
            else:
                request.session.pop('graphic_key')
            return iredirect('main:index')
        elif request.user.gr_key == gr_key:
            request.session['graphic_key'] = True
            return iredirect('main:index')
        return iredirect('accounts:login')
    return render(request, 'Accounts/GraphicKey.html', {'status': status})


def admin_login(request):
    p = urllib.parse.urlencode(request.GET)
    return redirect(f'{settings.LOGIN_URL}?' + p)


@login_required
def logout(request):
    auth.logout(request)
    return redirect(reverse('main:index'))


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(email=form.cleaned_data['email'],
                                            password=form.cleaned_data['fpassword'],
                                            last_name=form.cleaned_data['last_name'],
                                            first_name=form.cleaned_data['first_name'],
                                            surname=form.cleaned_data['surname'],
                                            dolzhnost=form.cleaned_data['dolzhnost'])
            auth.login(request, user)
            return iredirect('main:index')
        return render(request, 'Accounts/Registration.html', {'form': form})
    form = RegistrationForm()
    return render(request, 'Accounts/Registration.html', {'form': form})


@login_required
def change_password(request):
    if not request.method == 'POST':
        form = ChangePasswordForm(user=request.user)
        return render(request, 'Accounts/ChangePassword.html', {'form': form})
    # POST
    form = ChangePasswordForm(request.POST, user=request.user)
    if form.is_valid():
        request.user.set_password(form.cleaned_data['spassword'])
        request.user.save()
        auth.login(request, request.user)
        return redirect(reverse('accounts:personal_area'))
    return render(request, 'Accounts/ChangePassword.html', {'form': form})