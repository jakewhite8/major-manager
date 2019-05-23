from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Players, League, Team


class IndexView(generic.TemplateView):
  template_name = 'golf/index.html'

  def get_context_data(self):
    context = super(IndexView, self).get_context_data()
    context['Players'] = Players.objects.all().order_by('score')
    context['Team'] = Team.objects.all()
    return context

class PlayerView(generic.DetailView):
  model = Players
  template_name = 'golf/update.html'

  def get_queryset(self):
    return Players.objects.all()

def update(request, player_id):
  player = get_object_or_404(Players, pk=player_id)
  player.score = request.POST['score']
  player.save()

  return HttpResponseRedirect(reverse('golf:index'))