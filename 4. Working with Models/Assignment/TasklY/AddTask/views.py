from django.shortcuts import render,redirect
from . import forms    
def AddTask(request):
    if request.method == 'POST':
        form = forms.TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AddTask')
    else:   
        form = forms.TaskForm
        return render(request,'AddTask.html',{"form":form}) 
        