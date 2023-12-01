from django.shortcuts import render


def AppHome (request):
    return render(request,'AppHome.html')