from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import GolfCourse


@admin.register(GolfCourse)
class GolfCourse(SummernoteModelAdmin):
    """
    Golf Course model in admin panel
    """
    summernote_fields = ('content')
