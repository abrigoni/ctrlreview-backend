from django.db import models
from studios.models import Studio
from platforms.models import Platform
from genres.models import Genre


class Game(models.Model):
  title = models.CharField(max_length=200, unique=True)
  description = models.TextField()
  release_date = models.DateField(null=True)
  image_url = models.CharField(max_length=255)
  studio = models.ForeignKey(Studio, on_delete=models.DO_NOTHING)
  platforms = models.ManyToManyField(Platform)
  genres = models.ManyToManyField(Genre)

  def __str__(self):
    return self.title