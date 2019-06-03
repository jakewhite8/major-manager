from django.urls import path

from . import views

app_name = 'golf'
urlpatterns = [
  path('', views.IndexView.as_view(), name="index"),
  path('player/<int:player_id>/', views.PlayerView.as_view(), name="player"),
  path('player/<int:player_id>/update', views.update, name="update"),
  path('player/add_player/', views.AddPlayer.as_view(), name="add_player"),
  path('player/create', views.create_player, name="create_player"),
]