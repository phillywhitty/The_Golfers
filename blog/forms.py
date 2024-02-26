from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from . models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

