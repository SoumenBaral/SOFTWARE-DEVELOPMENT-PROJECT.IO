from django.db import models


class AddCategory(models.Model):
    CategoryName = models.CharField(max_length=200)
    

    def __str__ (self) -> str:
        return self.CategoryName