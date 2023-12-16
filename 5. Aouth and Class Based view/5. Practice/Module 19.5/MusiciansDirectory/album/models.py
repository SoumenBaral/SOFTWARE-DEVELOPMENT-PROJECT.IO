from django.db import models
from musician.models import Musician
from datetime import date
# Create your models here.
class Album(models.Model):
    AlbumName = models.CharField(max_length=100)
    Musician = models.ForeignKey(Musician,on_delete=models.CASCADE)
    releaseDate = models.DateTimeField(auto_now_add=True)
    Rating = models.ForeignKey('Ratings', on_delete=models.CASCADE)
    def __str__ (self) -> str:
        return self.AlbumName


class Ratings(models.Model):
    rating = models.CharField(max_length=100)

    def __str__(self):
        return self.rating