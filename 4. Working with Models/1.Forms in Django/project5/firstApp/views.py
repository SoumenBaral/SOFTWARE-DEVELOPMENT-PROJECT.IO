from django.shortcuts import render


def About(request):
    return render(request,'about.html')

def Form (request):
    if(request.method == "POST"):
        print(request.method)
    return render(request,'Form.html')
