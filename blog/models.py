from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils import timezone

STATUS = ((0, "Draft"), (1, "Published"))


# Custom Model

# ===========================================
# Golf Course Blog Model For User Profile
# ===========================================


class AddGolfCourse(models.Model):
    course_name = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    content = models.CharField(max_length=2000, blank=True)
    featured_image = CloudinaryField("image", default="placeholder")
    created_on = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, max_length=10, on_delete=models.CASCADE,
                             null=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.course_name} | written by {self.user}"


# ==========================
# Golf Course Comment Model
# ==========================


class Comment(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=2000)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    approved = models.BooleanField(default=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title
