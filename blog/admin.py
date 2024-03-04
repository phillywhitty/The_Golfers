from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import AddGolfCourse, Comment



@admin.register(AddGolfCourse)
class AddGolfCourse(SummernoteModelAdmin):
    """
   Adding a Golf Course model in admin panel
    """
    summernote_fields = ('content')


@admin.register(Comment)
class Comment(SummernoteModelAdmin):
    """
   Adding a Golf Course model in admin panel
    """
    summernote_fields = ('content')