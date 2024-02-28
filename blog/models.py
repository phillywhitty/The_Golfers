from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# models.py


class GolfCourse(models.Model):
    course_name = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    content = models.CharField(max_length=200, blank=True)
    created_on = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, max_length=10, on_delete=models.CASCADE, null=True)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    golf_course = models.ForeignKey(GolfCourse, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(default=False)
    date_published = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)


    @classmethod
    def default_golf_course(cls):
        return GolfCourse.objects.first(default=False)  

