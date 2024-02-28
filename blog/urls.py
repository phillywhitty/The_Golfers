from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing_page, name="landing_page"),
    path("about/", views.about, name="about"),
    path("blog_index/", views.blog_index, name="blog_index"),
    path("ballybunnion/", views.ballybunnion_blog, name="ballybunnion_blog"),
    path("doonbeg/", views.doonbeg_blog, name="doonbeg_blog"),
    path("k_club/", views.k_club_blog, name="k_club_blog"),
    path("create_blog/", views.create_blog, name="create_blog"),

    
]