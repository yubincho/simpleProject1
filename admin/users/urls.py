from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path("scrape", views.scrape, name="scrape"),
    # path("register/", views.register, name="register"),
    # path("login/", views.login, name="login"),
]
