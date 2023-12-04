from django.shortcuts import render
from . import models
# Create your views here.
def form(request):

    return render(request,'form.html')
