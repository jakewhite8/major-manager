from django.views import generic

from .models import Players, League, Team


class IndexView(generic.ListView):
  template_name = 'golf/index.html'
  context_object_name = 'players_list'

  def get_queryset(self):
    return Players.objects.all()