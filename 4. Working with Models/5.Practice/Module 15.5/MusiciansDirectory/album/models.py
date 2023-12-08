from django.db import models
from musician.models import Musician

# Create your models here.
class Album(models.Model):
    AlbumName = models.CharField(max_length=100)
    Musician = models.ForeignKey(Musician,on_delete=models.CASCADE)
    Email = models.EmailField(max_length=200)
    PhoneNumber = models.CharField(max_length=11)
    
    def __str__ (self) -> str:
        return self.FirstName


class Instrument(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name