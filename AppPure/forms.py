# -*- coding: utf-8 -*-
from django import forms
class AddForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)