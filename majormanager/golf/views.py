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

class PlayerView(generic.TemplateView):
  template_name = 'golf/update.html'

  def get_context_data(self, **kwargs):
    context = super(PlayerView, self).get_context_data()
    context['Player'] = Players.objects.get(pk=kwargs['player_id'])
    context['Teams'] = Team.objects.all()
    return context

class AddPlayer(generic.TemplateView):
  template_name = 'golf/add_player.html'

def update(request, player_id):
  player = get_object_or_404(Players, pk=player_id)
  
  # if a players score has been provided, update it
  # need to throw an error here when the score is not a valid number
  def is_digit(number):
    try:
      int(number)
      return True
    except ValueError:
      return False

  if len(request.POST['score']) and is_digit(request.POST['score']):
    player.score = request.POST['score']
    player.save()
  
  # compare the players current list of teams with the ones submitted 
  # and updated accordingly
  players_current_teams = [team.id for team in player.team_set.all()]
  if len(players_current_teams):
    players_current_teams.sort()

  updated_team_ids = request.POST.getlist('team')
  if len(updated_team_ids):
    updated_team_ids.sort()

  if players_current_teams != updated_team_ids:
    # make a list of the players new Team set based off 
    # the ids recieved from the request
    updated_teams = Team.objects.filter(id__in=updated_team_ids)
    player.team_set.set(updated_teams)

  return HttpResponseRedirect(reverse('golf:index'))

def delete_player(request, player_id):
  player = get_object_or_404(Players, pk=player_id)
  player.delete()
  return HttpResponseRedirect(reverse('golf:index'))

def create_player(request):
  new_player_name = request.POST['player_name']
  new_player_score = request.POST['score']
  new_player = Players(player_name=new_player_name, score=new_player_score)
  new_player.save()
  return HttpResponseRedirect(reverse('golf:index'))
