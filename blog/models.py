from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.text import slugify
from django.urls import reverse

STATUS = ((0, "Draft"), (1, "Published"))

#-------------------------------#
# Custom Model
# ==============================
# Add Golf Course Blog Model
# ==============================
class AddGolfCourse(models.Model):
    course_name = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    content = models.CharField(max_length=200, blank=True)
    created_on = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, max_length=10, on_delete=models.CASCADE, null=True)


# ===============================================
#  Post Blog Model
# ===============================================

class Post(models.Model):
    content = models.TextField(max_length=100, blank=True)
    created_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    

