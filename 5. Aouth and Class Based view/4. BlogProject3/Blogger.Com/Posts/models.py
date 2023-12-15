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

class Comment(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True) # jkhn e ei class er object toiri hobe sei time ta rekhe dibe
    
    def __str__(self):
        return f"Comments by {self.name}"