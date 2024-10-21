
from django import forms
from django.core.exceptions import ValidationError
from .models import Url, Setting
from django.core.exceptions import NON_FIELD_ERRORS
import re
from datetime import datetime, date, time

class SettingForm(forms.ModelForm):
    class Meta:
        model = Setting
        fields = ['name', 'key', 'value']
class UrlForm(forms.ModelForm):
    class Meta:
        model = Url
        fields = ['name', 'link', 'mentionto']
