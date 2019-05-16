from django.db import models

class League(models.Model):
  league_name = models.CharField(max_length=200)

  def __str__(self):
    return self.league_name

class Players(models.Model):
  player_name = models.CharField(max_length=200)
  score = models.IntegerField(null=True)

  def __str__(self):
    return self.player_name

class Team(models.Model):
  league = models.ForeignKey(League, on_delete=models.CASCADE)
  players = models.ManyToManyField(Players)
  team_name = models.CharField(max_length=200)

  def __str__(self):
    return self.team_name

  def get_score(self):
    score = 0
    for player in self.players.all():
      if isinstance(player.score, int):
        score += player.score
    return score
