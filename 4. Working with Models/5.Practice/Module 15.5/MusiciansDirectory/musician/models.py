from django.db import models

# Create your models here.
class Musician(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Email = models.EmailField(max_length=200)
    PhoneNumber = models.IntegerField(max_length=11)
    INSTRUMENT_CHOICES = [
        ('guitar', 'Guitar'),
        ('piano', 'Piano'),
        ('drums', 'Drums'),
        
    ]
    
    Instruments = models.ManyToManyField('Instrument',)
    def __str__ (self) -> str:
        return self.FirstName


class Instrument(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name