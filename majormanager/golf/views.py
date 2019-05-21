from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Players, League, Team


class IndexView(generic.ListView):
  template_name = 'golf/index.html'
  context_object_name = 'players_list'

  def get_queryset(self):
    return Players.objects.all().order_by('score')

class PlayerView(generic.DetailView):
  model = Players
  template_name = 'golf/update.html'

  def get_queryset(self):
    return Players.objects.all()