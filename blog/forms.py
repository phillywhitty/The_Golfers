from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from . models import AddGolfCourse


class CreateGolfBlogForm(ModelForm):

    class Meta:
        model = AddGolfCourse
        fields = ['course_name', 'location', 'content',]
        exclude = ['user',]


class CreateUserForm(forms.ModelForm):

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']



class UpdateUserForm(forms.ModelForm):

    password = None

    class Meta:
        model = User
        fields = ['username', 'email',]
        exclude = ['password1', 'password2',]

