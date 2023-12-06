from django.db import models


class MyModel(models.Model):
    auto_field = models.AutoField(primary_key=True)
    name = models.CharField(max_length= 20)
    bol = models.BooleanField()
    date_field = models.DateField()
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
    duration_field = models.DurationField()
    email_field = models.EmailField()
    file_field = models.FileField(upload_to='files/')
    integer_field = models.IntegerField()
    json_field = models.JSONField()