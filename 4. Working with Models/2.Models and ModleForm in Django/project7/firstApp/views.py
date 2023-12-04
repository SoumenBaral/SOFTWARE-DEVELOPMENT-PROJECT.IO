from django.shortcuts import render,redirect
from . import models
# Create your views here.
def form(request):
    student = models.Student.objects.all()
    
    return render(request,'form.html',{"data":student})
def delete_student(request,roll):
    std = models.Student.objects.get(pk=roll).delete()
    print(std)
    return redirect("homepage")