from django.shortcuts import render,redirect
from . import models,forms
# Create your views here.
def form(request):
    student = models.Student.objects.all()
    
    return render(request,'form.html',{"data":student})
def delete_student(request,roll):
    std = models.Student.objects.get(pk=roll).delete()
    print(std)
    return redirect("homepage")

def add_student(request):
    if request.method == 'POST':
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("homepage")
    else :
        form = forms.StudentForm()
    return render(request, 'add_student.html', {'form' : form})