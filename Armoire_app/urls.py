from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("addpiece", views.add_piece, name="addpiece"),
    path("mycloset", views.my_closet, name="mycloset"),
    path("outfit/<str:outfit_id>", views.outfit, name="outfit"),
    path("piecetooutfit/<int:piece_id>&<int:outfit_id>", views.piecetooutfit, name="piecetooutfit"),
    path("deletepiece/<int:piece_id>", views.deletepiece, name="deletepiece"),
    path("deleteoutfit/<int:outfit_id>", views.deleteoutfit, name="deleteoutfit"),

]
