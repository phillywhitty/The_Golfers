from django.urls import path
from . import views

#--------------------- Url Paths---------------------#

urlpatterns = [
    path("", views.landing_page, name="landing_page"),
    path("about/", views.about, name="about"),
    path("popular_courses/", views.popular_courses, name="popular_courses"),
    path("create_blog/", views.create_blog, name="create_blog"),
    path("my_golf_blog/", views.my_golf_blog, name="my_golf_blog"),
    path("update_blog/<str:pk>", views.update_blog, name="update_blog"),
    path("delete_blog/<str:pk>", views.delete_blog, name="delete_blog"),
    path("profile/", views.profile, name="profile"),
    path("profile_delete/", views.profile_delete, name="profile_delete"),
]
