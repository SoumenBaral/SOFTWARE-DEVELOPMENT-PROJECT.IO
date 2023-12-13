from django.shortcuts import render
from Posts.models import Posts,Category

def Home(request,category_slug = None):
    data = Posts.objects.all()
    if category_slug is not None: # ekhn category slug jodi None na hoy tar mane sekhane value ache
        category = Category.objects.get(slug = category_slug) # slug je field model e likhechilam seta = amader category slug kore dilam taile ekhn kon category er slug sei category object peye jabo
        data = Posts.objects.filter(category  = category) # post er category te category object bosiye filter korlam, ager data er sathe overright hoye jabe
    
    Categories = Category.objects.all()
    return render(request,'home.html',{"data":data,"Categories":Categories})