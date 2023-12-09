from django.shortcuts import render,redirect
from . import forms
from . import models    
def AddTask(request):
    if request.method == 'POST':
        form = forms.TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showTask')
    else:   
        form = forms.TaskForm
        return render(request,'AddTask.html',{"form":form}) 

def EditTask(request,id):
    post = models.TaskModel.objects.get(pk=id)
    if request.method == 'POST':
        form = forms.TaskForm(request.POST ,instance=post)
        if form.is_valid():
            form.save()
            return redirect('showTask')
    else:
        form = forms.TaskForm(instance=post)
        return  render(request,'AddTask.html',{"form":form})
def DeleteTask(request,id):
    post = models.TaskModel.objects.get(pk=id)
    post.delete()
    return redirect('home')