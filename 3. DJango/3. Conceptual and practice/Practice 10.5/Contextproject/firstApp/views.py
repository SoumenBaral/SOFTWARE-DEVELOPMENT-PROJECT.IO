from django.shortcuts import render
from datetime import date

current_date = date.today()

def AppHome (request):
    dec = {"fun":['python', 'is', 'fun'] , "today":current_date,'Nodata':"","adding":10,"MyName": "soumen",
           'fundus':"Mama Mia Man Make My Money Maker",
           "sortBy" : [
                        {'name': 'Josh', 'age': 19},
                        {'name': 'Dave', 'age': 22},
                        {'name': 'Joe', 'age': 31},
                    ]
           }
    return render(request,'AppHome.html',dec)