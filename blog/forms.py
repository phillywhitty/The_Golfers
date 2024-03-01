from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.models import User, UserCreationForm
from . models import AddGolfCourse


class CreateGolfBlogForm(ModelForm):

    class Meta:
        model = AddGolfCourse
        fields = ['course_name', 'location', 'content',]
        exclude = ['user',]


class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']



class UpdateUserForm(forms.ModelForm):

    password = None

    class Meta:
        model = User
        fields = ['username', 'email',]
        exclude = ['password1', 'password2',]

