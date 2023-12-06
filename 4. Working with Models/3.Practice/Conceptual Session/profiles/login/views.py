from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(request):
    # return HttpResponse("<h1 style='text-align:center;'>ami to vala na </h1>")
    return render(request,'home.html')

def Login(request):
    return render(request,'login.html')