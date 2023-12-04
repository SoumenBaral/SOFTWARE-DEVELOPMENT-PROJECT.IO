from django.shortcuts import render
from . import models
# Create your views here.
def form(request):
    student = models.Student.objects.all()
    
    return render(request,'form.html',{"data":student})
def delete_student(request,roll):
    std = models.Student.objects.get()
    print(std)