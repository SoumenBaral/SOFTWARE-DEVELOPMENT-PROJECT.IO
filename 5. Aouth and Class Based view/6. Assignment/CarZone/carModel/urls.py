from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.AddPostCreateView.as_view(),name="addCar"),
    
    # # path('edit/<int:id>',views.EditPost, name='edit'),
    # path('edit/<int:id>/',views.UpdatePost.as_view(), name='edit'),

    # # path('delete/<int:id>',views.DeletePost, name='delete'),

    # path('delete/<int:id>/',views.DeleteViewed.as_view(), name='delete'),

    path('details/<int:id>/',views.DetailsPost.as_view(),name="details_view"),
    path('buy_car/<int:id>/',views.DetailsPost.as_view(),name='buyCar')

]