from django.shortcuts import render
from django.views.generic import TemplateView

def home (request):
    return render(request,'Home.html')

class Home(TemplateView):
    template_name = 'Home.html'