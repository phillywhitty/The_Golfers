
from django.contrib import admin
from django.urls import path, include
from django.urls import path, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('blog.urls'), name='blog_urls'),
    path('accounts/', include('allauth.urls'))
]
