from django.shortcuts import render
from django.http import HttpResponse



def Home(request):
    d = {"name":"Soumen","age":5,"list":[1,2,3,"ami",'tumi','danish'],
         "course": [
             {
                 "Id":1,
                 "name":"Python",
                 "fee":5000                 
             },
             {
                 "Id":2,
                 "name":"django",
                 "fee":15000                 
             },
             {
                 "Id":3,
                 "name":"React",
                 "fee":5000                 
             },
         ]
         
         }
    return render(request,'Home.html',d)

def About (request):
    return HttpResponse("Ami to Vala na vala loia thiko ")
