from django.shortcuts import render


def navHome(request):
    return render(request,"nav/navHome.html")