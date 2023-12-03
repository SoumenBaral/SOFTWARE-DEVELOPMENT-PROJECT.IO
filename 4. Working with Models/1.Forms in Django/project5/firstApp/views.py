from django.shortcuts import render


def About(request):
    return render(request,'about.html')

def Form (request):
    return render(request,'Form.html')
