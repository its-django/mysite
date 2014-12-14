#!/usr/bin/env python
# encoding: utf-8

from django import forms


class CommentForm(forms.Form):

    """Comment Form class clear"""

    visitor = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=20, required=False)
    content = forms.CharField(max_length=200, widget=forms.Textarea())
