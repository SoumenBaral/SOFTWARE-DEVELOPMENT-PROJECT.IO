from django.shortcuts import render
from datetime import date

current_date = date.today()

def AppHome (request):
    dec = {"fun":['python', 'is', 'fun'] , "today":current_date,'Nodata':""}
    return render(request,'AppHome.html',dec)