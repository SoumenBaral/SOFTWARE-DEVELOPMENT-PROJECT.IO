from django.db import models
from AddCategory.models import AddCategory
class TaskModel(models.Model):

    taskTitle= models.CharField(max_length=200)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    AssignDate = models.DateField()
    category = models.ManyToManyField(AddCategory)
    def __str__(self):
        return self.taskTitle

   

