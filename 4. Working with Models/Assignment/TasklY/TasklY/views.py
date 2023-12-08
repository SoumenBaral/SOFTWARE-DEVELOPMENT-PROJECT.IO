from django.shortcuts import render
from AddCategory.models import AddCategory
def Home(request):
    return render(request,'Home.html')

def ShowTask(request):
    data = AddCategory.objects.all()
    return render(request,'ShowTask.html',{"data":data})