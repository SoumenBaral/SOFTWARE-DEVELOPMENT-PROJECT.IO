from django.db import models
from Categories.models import Category
from Author.models import Author
# Create your models here.

class Posts(models.Model):
    Name  = models.CharField(max_length=100)
    Content = models.TextField()
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)

    def __str__ (self):
        return self.Name
    