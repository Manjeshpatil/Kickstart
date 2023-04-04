
from django.urls import path
from . import views


urlpatterns = [
    path("", views.HomePage, name="home"),
    path("logout/", views.LogoutPage, name="logout" ),
     path("register/", views.RegisterPage, name="register"  ),
      path("login/", views.LoginPage, name="login"  ),
]
