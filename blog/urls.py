from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing_page, name="landing_page"),
    path("about/", views.about, name="about"),
    path("index/", views.index, name="index"),
    path("ballybunnion/", views.ballybunnion_blog, name="ballybunnion_blog"),
    path("doonbeg/", views.doonbeg_blog, name="doonbeg_blog"),
    path("k_club/", views.k_club_blog, name="k_club_blog"),
    
]