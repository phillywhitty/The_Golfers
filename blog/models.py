from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# models.py


class GolfCourse(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='golf_course_images')


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    golf_course = models.ForeignKey(GolfCourse, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(default=False)
    date_published = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    # Provide a default value for existing rows when adding a non-nullable field
    @classmethod
    def default_golf_course(cls):
        return GolfCourse.objects.first(default=False)  # Change this default as per your requirements

