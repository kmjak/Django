from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('plast/', views.lastPage, name='plast'),
    path('msgs/<int:page>/', views.msgs,name='msgs'),
    path('msgs/', views.msgs,name='msgs'),
    path('usr/', views.userName, name='usr'),
    path('usr/<int:user_id>/', views.userName,name='usr'),
    path('post/', views.post, name='post'),
    path('good/<int:msg_id>/', views.good, name='good'),
]