from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("add", views.add_todo, name="add_todo"),
    path("update/<int:id>", views.update, name="update"),
    path("delete/<int:id>", views.delete_todo, name="delete")

]