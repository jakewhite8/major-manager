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
    # create an array with all of a teams scores in it
    # sort the array from lowest to highest
    # return the total of the four best scores 
    scores = []
    for player in self.players.all():
      if isinstance(player.score, int):
        scores.append(player.score)

    def aggregate_of_top_four_scores(array):
      total_score = 0
      for score in array:
        total_score += score
      return total_score

    if len(scores):
      scores.sort()
      return aggregate_of_top_four_scores(scores[:4])
    else:
      return False
