from django.contrib import admin
from django.urls import path, include
from django.urls import path, re_path
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('', include('home.urls')),
    path('blog/', include('blog.urls')),
    
]
