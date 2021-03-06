from django.urls import path

from . import views

app_name = 'golf'
urlpatterns = [
  path('', views.IndexView.as_view(), name="index"),
  path('player/<int:player_id>/', views.PlayerView.as_view(), name="player"),
  path('player/<int:player_id>/update', views.update, name="update"),
  path('player/<int:player_id>/delete_player', views.delete_player, name="delete_player"),
  path('player/add_player/', views.AddPlayerView.as_view(), name="add_player"),
  path('team/add_team/', views.AddTeamView.as_view(), name="add_team"),
  path('team/<int:team_id>/', views.TeamView.as_view(), name="team"),
  path('team/<int:team_id>/update', views.update_team, name="update_team"),
  path('player/create', views.create_player, name="create_player"),
  path('team/create', views.create_team, name="create_team"),
]