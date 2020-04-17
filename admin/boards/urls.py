from django.urls import path
from . import views

urlpatterns = [
    path("list/", views.board_list, name="board_list"),
    path("detail/<int:board_id>", views.board_detail, name="board_detail"),
    path("", views.search_result, name="search_result"),
]
