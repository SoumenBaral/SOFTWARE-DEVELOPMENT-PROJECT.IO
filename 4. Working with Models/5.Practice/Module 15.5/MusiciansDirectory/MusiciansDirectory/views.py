from django.shortcuts import render
from album.models import Album
def Home(request):
    data = Album.objects.all()
    return render(request,'home.html',{"data":data})