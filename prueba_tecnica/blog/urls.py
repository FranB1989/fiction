from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.index_view, name="index"),
    path("create/", views.create_blog_entry, name="create_blog"),
    path("post/<int:pk>/delete/", views.delete_blog_entry, name="delete_blog_entry"),
]
