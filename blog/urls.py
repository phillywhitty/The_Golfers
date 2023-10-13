from . import views
from django.urls import include, path
from allauth import account

urlpatterns = [
     path('', views.landing_page, name='landing_page'),
     path('home', views.landing_page, name='home'),
     path("about/", views.about, name="about"),
     # path('login/', account.views.LoginView.as_view(), name='custom_login'),
     path('signin/', views.custom_login, name='custom_signin'),
     path("post_list/", views.PostList.as_view(), name="index"),
     path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail')
]