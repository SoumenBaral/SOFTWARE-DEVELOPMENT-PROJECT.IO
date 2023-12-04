from django.shortcuts import render
from . import models
# Create your views here.
def form(request):
    student = models.Student.objects.all()
    
    return render(request,'form.html',{"data":student})
