from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import GolfCourse, Comment

@admin.register(GolfCourse)
class GolfCourseAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'golf_course', 'text', 'date_published', 'approved')
    list_filter = ('approved',)
    search_fields = ('text',)
