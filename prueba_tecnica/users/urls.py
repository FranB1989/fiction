from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path("", views.home_view, name="home"),
    path("create_account/", views.register_view, name="create_account"),
    path("login/", views.login_view, name="login"),
    path("password_reset/", views.password_reset_view, name="password_reset"),
]
