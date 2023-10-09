from . import views
from django.urls import include, path


urlpatterns = [
     path('', views.landing_page, name='landing_page'),
     path("about/", views.about, name="about"),
     path("index/", views.index, name="index"),
]