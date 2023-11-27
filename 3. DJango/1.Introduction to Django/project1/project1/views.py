from django.http import HttpResponse

def contact(request):
    return  HttpResponse("Hello world ! ")

def home(request):
    return HttpResponse("Welcome home ")