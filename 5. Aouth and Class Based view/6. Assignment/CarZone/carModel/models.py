from django.db import models
from carsBrand.models import Brand
from django.contrib.auth.models import User


class AddCar(models.Model):
    Name  = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=0 , default=0.00)
    quantity = models.IntegerField(default=0)
    Content = models.TextField()
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE,)
    image = models.ImageField(upload_to='carModel/media/uploads/', blank = True, null = True)

    def __str__ (self):
        return self.Name

class Comment(models.Model):
    post = models.ForeignKey(AddCar, on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comments by {self.name}"