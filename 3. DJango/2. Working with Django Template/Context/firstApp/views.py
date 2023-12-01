from django.shortcuts import render
from django.http import HttpResponse



def Home(request):
    d = {"name":"Soumen","Age":25,"list":[1,2,3,"ami",'tumi','danish']}
    return render(request,'Home.html',d)

def About (request):
    return HttpResponse("Ami to Vala na vala loia thiko ")
