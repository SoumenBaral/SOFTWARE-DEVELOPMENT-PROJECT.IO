from django.shortcuts import render
from Posts.models import Posts,Category

def Home(request):
    data = Posts.objects.all()
    Categories = Category.objects.all()
    # print(data)
    # for i in data:
    #     print(i.Name)
    #     for j in i.Category.all():
    #         print(j)

    return render(request,'home.html',{"data":data,"Categories":Categories})