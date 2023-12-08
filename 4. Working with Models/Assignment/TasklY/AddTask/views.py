from django.shortcuts import render

def AddTask(request):
    return render(request,'AddTask.html')
