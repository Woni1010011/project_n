from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="main"),
    path("search", views.search, name="search"),
    path("material_search", views.material_search, name="material_search"),
    path("img_search", views.img_search, name="img_search"),
    path("board", views.board, name="board"),
    path("search_result", views.search_result, name="search_result"),
    path("mypage", views.mypage, name="mypage"),
    path("profile_edit", views.profile_edit, name="profile_edit"),
    path('post/<int:recipe_no>/', views.post, name='post'),
    path("write_post", views.write_post, name="write_post"),
]
