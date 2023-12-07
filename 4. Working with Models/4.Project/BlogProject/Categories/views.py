from django.shortcuts import render

# Create your views here.
def AddCategories(request):
    return render(request,'Categories.html')