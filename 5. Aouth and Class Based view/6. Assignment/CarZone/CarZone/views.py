from django.shortcuts import render
from carModel.models import AddCar,Brand

def Home(request,brand_slug = None):
    data = AddCar.objects.all()
    if brand_slug is not None: 
        brand = Brand.objects.get(slug = brand_slug) 
        data = AddCar.objects.filter(brand  = brand)
    
    Brands = Brand.objects.all()
    return render(request,'Home.html',{"data":data,"Brands":Brands})