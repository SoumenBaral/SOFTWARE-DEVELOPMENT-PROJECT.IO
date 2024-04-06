from django.shortcuts import render
from datetime import datetime , timedelta
from django.http import HttpResponse
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
    request.session['name'] = 'Karim'
    return render(request,'set_session.html')

def get_session(request):
    if 'name' in request.session:
        name = request.session.get('name', 'Guest')
        request.session.modified = True
        return render(request,'get_session.html' ,{'name' : name})
    else:
        return HttpResponse("Your session has been expired.Login again")


    # name = request.session.get('name', 'Guest')
    # return render(request,'get_session.html' ,{'name' : name})
        
def del_session(request):
    # del request.session['name']
    request.session.flush()
    return render(request,'del_session.html')
