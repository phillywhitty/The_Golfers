from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from . models import AddGolfCourse
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


# Define a form for creating golf blog entries
class CreateGolfBlogForm(ModelForm):

    class Meta:
        model = AddGolfCourse
        fields = ['course_name', 'location', 'content', ]
        exclude = ['user', ]


# Define a form for updating user information
class UpdateUserForm(forms.ModelForm):

    password = None

    class Meta:
        model = User
        fields = ['username', 'email', ]
        exclude = ['password1', 'password2', ]
