from django.shortcuts import render

# Create your views here.
def AddCat(request):
    return render(request,'AddCat.html')