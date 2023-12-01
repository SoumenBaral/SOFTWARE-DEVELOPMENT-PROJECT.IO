from django.shortcuts import render

def Home(req):
    return render(req,'Home.html')