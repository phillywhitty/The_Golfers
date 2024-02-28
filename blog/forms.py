from django.forms import ModelForm
from django.contrib.auth.models import User
from . models import GolfCourse, Comment


class CreateBlogForm(ModelForm):
    class Meta:
        model = GolfCourse
        fields = ['course_name', 'location', 'content',]
        exclude = ['user',]
