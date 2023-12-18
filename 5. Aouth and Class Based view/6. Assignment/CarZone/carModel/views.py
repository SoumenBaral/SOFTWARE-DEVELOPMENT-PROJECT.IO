from django.shortcuts import render
from . import models,forms
from django.views.generic import CreateView ,UpdateView,DeleteView,DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.
@method_decorator(login_required, name= 'dispatch') 
class AddPostCreateView(CreateView):
    model = models.AddCar
    form_class = forms.AddCarForm
    template_name = "addCar.html"
    def get_success_url(self):
        return reverse_lazy('home')
    
    def form_valid(self, form):
        messages.success(self.request, 'Successfully Added Car')
        return super().form_valid(form)
    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.warning(self.request,"can't not create Post For this Car ")
        return response

class DetailsPost(DetailView):
    model = models.AddCar
    pk_url_kwarg = 'id'
    template_name = 'carDetails.html'
    def post(self,request,*args,**kwargs):
        comment_form = forms.CommentForm(data = self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit = False)
            new_comment.post = post 
            new_comment.save()
        if 'buy_car' in request.POST:
            if post.quantity > 0:
                post.quantity -=1
                post.save()
                models.BuyCar.objects.create(user=request.user, car=post)
            else:
                messages.warning(self.request, 'All Car is Sold out please look forward')
        return self.get(request, *args,**kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.comments.all()
        comment_form = forms.CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context