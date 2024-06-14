from django.urls import path
from . import views
from .views import ProductsList,ProductsDetail

urlpatterns = [
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('list',ProductsList.as_view(),name='list'),
    path('detail/<int:pk>',ProductsDetail.as_view(),name='detail'),
    path('edit/<int:p_id>',views.edit,name='edit'),
    path('delete/<int:p_id>',views.delete,name='delete'),
]