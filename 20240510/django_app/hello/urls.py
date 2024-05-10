from django.urls import path
from . import views

urlpatterns = [
    # path('<int:id>/<nickname>/', views.index, name='index'),
    path('', views.index, name='index'),
    # path('form', views.form, name='form'),
    # path('next', views.next, name='next'),
    # path('test', views.test, name='test'),
]