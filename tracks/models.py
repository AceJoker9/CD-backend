from django.db import models

# Create your models here.
class Tracks(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    release_date = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)