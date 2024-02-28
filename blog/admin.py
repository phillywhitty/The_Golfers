from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import GolfCourse, Comment


@admin.register(GolfCourse)
class GolfCourse(SummernoteModelAdmin):
    """
    Golf Course model in admin panel
    """
    summernote_fields = ('content')

admin.site.register(Comment)