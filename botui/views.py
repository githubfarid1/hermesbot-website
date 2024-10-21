from django.shortcuts import render
import os
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from .models import Url, Setting
import json
from .forms import UrlForm, SettingForm
from django.http import HttpResponse, Http404, JsonResponse
from django.views.decorators.http import require_POST
from sys import platform
from subprocess import Popen, check_call, call, run, PIPE
import psutil
import linecache
import time
from django.conf import settings
from django.db.models import Q
from django.contrib.auth.decorators import login_required

@login_required(login_url="login")
def show_settings(request):
    context = {
    }
    return render(request=request, template_name='botui/show_settings.html', context=context)

@login_required(login_url="login")
def setting_list(request):
    settings = Setting.objects.all()
    return render(request, 'botui/setting_list.html', {
        'data': settings,
    })

@login_required(login_url="login")
def edit_setting(request, pk):
    setting = get_object_or_404(Setting, pk=pk)
    # return HttpResponse(year.id)
    if request.method == "POST":
        form = SettingForm(request.POST, instance=setting)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "settingListChanged": None,
                        "showMessage": f"{setting.name} updated."
                    })
                }
            )
    else:
        form = SettingForm(instance=setting)
    return render(request, 'botui/setting_form.html', {
        'form': form,
        'setting': setting,
        'module': 'Edit Data'
    })

@login_required(login_url="login")
def add_setting(request):
    if request.method == "POST":
        form = SettingForm(request.POST)
        if form.is_valid():
            setting = form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "settingListChanged": None,
                        "showMessage": f"{setting.key} added."
                    })
                })
    else:
        form = SettingForm()
    return render(request, 'botui/setting_form.html', {
        'form': form,
        'module': 'Add Data'
    })

@login_required(login_url="login")
def show_urls(request):
    context = {
    }
    return render(request=request, template_name='botui/show_urls.html', context=context)

@login_required(login_url="login")
def url_list(request):
    urls = Url.objects.all()
    return render(request, 'botui/url_list.html', {
        'data': urls,
    })

@login_required(login_url="login")
def add_url(request):
    if request.method == "POST":
        form = UrlForm(request.POST)
        if form.is_valid():
            url = form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "urlListChanged": None,
                        "showMessage": f"{url.name} added."
                    })
                })
    else:
        form = UrlForm()
    return render(request, 'botui/url_form.html', {
        'form': form,
        'module': 'Add Data'
    })

@login_required(login_url="login")
def edit_url(request, pk):
    url = get_object_or_404(Url, pk=pk)
    # return HttpResponse(year.id)
    if request.method == "POST":
        form = UrlForm(request.POST, instance=url)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "urlListChanged": None,
                        "showMessage": f"{url.name} updated."
                    })
                }
            )
    else:
        form = UrlForm(instance=url)
    return render(request, 'botui/proxy_form.html', {
        'form': form,
        'proxy': url,
        'module': 'Edit Data'
    })

@login_required(login_url="login")
def remove_url(request, pk):
    url = get_object_or_404(Url, pk=pk)
    url.delete()
    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "urlListChanged": None,
                "showMessage": f"{url.name} deleted."
            })
        })
