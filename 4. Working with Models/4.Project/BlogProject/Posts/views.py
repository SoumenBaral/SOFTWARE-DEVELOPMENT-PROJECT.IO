from django.shortcuts import render

# Create your views here.
def AddPost(request):
    return  render(request,'Posts.html')