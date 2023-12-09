from django.shortcuts import render
from AddTask.models import TaskModel
def Home(request):
    return render(request,'Home.html')

def ShowTask(request):
    data = TaskModel.objects.all()
    return render(request,'ShowTask.html',{"data":data})