from django.shortcuts import render
from django.http import HttpResponse



def Home(request):
    return render(request,'Home.html')

def About (request):
    return HttpResponse("Ami to Vala na vala loia thiko ")
