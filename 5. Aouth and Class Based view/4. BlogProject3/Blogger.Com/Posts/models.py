from django.db import models
from Categories.models import Category
from django.contrib.auth.models import User
# from Author.models import Author
# Create your models here.

class Posts(models.Model):
    Name  = models.CharField(max_length=100)
    Content = models.TextField()
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Posts/media/uploads/', blank = True, null = True)

    def __str__ (self):
        return self.Name
    