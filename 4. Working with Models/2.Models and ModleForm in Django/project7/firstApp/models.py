from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=30)
    roll = models.IntegerField(primary_key=True)
    address = models.TextField()
    father_name = models.TextField(default="Shyamal chandra baral")

    def __str__(self):
        return f'Roll:{self.roll}--{self.name}'
    

