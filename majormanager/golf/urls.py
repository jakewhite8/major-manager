from django.urls import path

from . import views

app_name = 'golf'
urlpatterns = [
  path('', views.IndexView.as_view(), name="index"),
  path('player/<int:pk>/', views.PlayerView.as_view(), name="player"),
  path('player/<int:player_id>/update', views.update, name="update"),
]