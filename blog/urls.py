from . import views
from django.urls import path


urlpatterns = [
     path("", views.landing_page, name="landing_page"),
     path("", views.landing_page, name="landing_page"),
     path("about/", views.about, name="about"),
]