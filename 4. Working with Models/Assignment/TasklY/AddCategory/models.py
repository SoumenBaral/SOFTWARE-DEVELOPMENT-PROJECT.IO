from django.db import models
from AddTask.models import TaskModel

class AddCategory(models.Model):
    CategoryName = models.CharField(max_length=200)
    CategoryIsFor = models.ManyToManyField(TaskModel)

    def __str__ (self) -> str:
        return self.CategoryName