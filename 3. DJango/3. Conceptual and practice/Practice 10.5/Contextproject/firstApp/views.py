from django.shortcuts import render


def AppHome (request):
    dec = {"fun":['python', 'is', 'fun'] , "today": "2023-01-12T10:30:00.000123"}
    return render(request,'AppHome.html',dec)