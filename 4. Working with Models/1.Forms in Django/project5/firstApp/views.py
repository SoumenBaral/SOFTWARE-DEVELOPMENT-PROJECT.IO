from django.shortcuts import render
from .forms import contactForm

def About(request):
    if(request.method == "POST"):
        print(request.POST)
        name =request.POST.get("username")
        email =request.POST.get("email")
        select =request.POST.get("select")
        return render(request,'about.html',{"name":name,"email":email,'select':select})
    return render(request,'about.html')

def Form (request):       
    return render(request,'Form.html')


# def DjangoForm(request):
#     form = contactForm(request.POST)
#     if form.is_valid():
#         print(form.cleaned_data)
#     return render(request,'django_form.html',{"form":form})
# want to upload file 

# def DjangoForm(request):
#     form = contactForm(request.POST,request.FILES)
#     if form.is_valid():
#         file =form.cleaned_data['file']
#         with open('./firstApp/uploads/' + file.name, 'wb+') as destination:
#             for chunk in file.chunks():
#                 destination.write(chunk)
#         print(form.cleaned_data)
#     else:
#         form = contactForm()

#     return render(request,'django_form.html',{"form":form})


def DjangoForm(request):
    if request.method == 'POST':
        form = contactForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            with open('./firstApp/uploads' + file.name, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            print(form.cleaned_data)
    else:
        form = contactForm()
    return render(request, 'django_form.html', {'form':form}) 