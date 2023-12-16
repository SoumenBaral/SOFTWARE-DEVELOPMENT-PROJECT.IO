from django.shortcuts import render
from datetime import datetime , timedelta

# Create your views here.
def setCookie(request):
    response = render(request,'Home.html')
    response.set_cookie('name','aLa')
    response.set_cookie('name','khat',expires=datetime.utcnow()+timedelta(days=7))

    return response

def getCookies(request):
    name = request.COOKIES.get('name')
    print(request.COOKIES)
    return render(request,'getCookies.html',{"name":name})

def deleteCookies(request):
    response = render(request,'deleteCookies.html')
    response.delete_cookie('name')
    return response

def setSession(request):
    data = {
        'name' : 'rahim',
        'age' : 23,
        'language' : 'Bangla'
      }