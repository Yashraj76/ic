from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name='index-page'),
    path("register/",views.register,name='register-page'),
    path("home/",views.home,name='home-page'),
    path("profile/",views.profile,name='profile-page'),
]
