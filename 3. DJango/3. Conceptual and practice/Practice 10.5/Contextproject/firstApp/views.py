from django.shortcuts import render
from datetime import date ,datetime

current_date = date.today()
current_time = datetime.now().time()
def AppHome (request):
    dec = {"fun":['python', 'is', 'fun'] , "today":current_date,'Nodata':"","adding":10,"MyName": "soumen",
           'fundus':"Mama Mia Man Make My Money Maker",
           "sortBy" : [
                        {'name': 'Josh', 'age': 19},
                        {'name': 'Dave', 'age': 22},
                        {'name': 'Joe', 'age': 31},
                    ],
            "current_time":current_time
           }
    return render(request,'AppHome.html',dec)