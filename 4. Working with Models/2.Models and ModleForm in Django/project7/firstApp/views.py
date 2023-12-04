from django.shortcuts import render
from . import models
# Create your views here.
def form(request):
    student = models.Student.objects.all()
    print(student)
    return render(request,'form.html')
