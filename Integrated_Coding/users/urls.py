from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name='index-page'),
    path("register/",views.register,name='register-page'),
    path("home/",views.home,name='home-page'),
    path("profile/",views.profile,name='profile-page'),
    path("edit_profile/",views.edit_profile,name='edit-profile'),
    path("homepage/",views.homepage,name='homepage-page')
]
