from . import views
from django.urls import include, path
from allauth import account
from .views import KClubPosts

urlpatterns = [
     path('', views.home, name='home'),
     path("post_list/", views.PostList.as_view(), name="index"),
     path("about/", views.about, name="about"),
     path('signin/', views.custom_login, name='custom_signin'),
     path("post_list/", views.PostList.as_view(), name="index"),
     path('k_club', views.k_club, name='k_club'),
     path('k_club_posts', KClubPosts.as_view(), name='k_club_posts'),
]