from django.urls import path
from .views import HelloView

urlpatterns = [
    # path('<int:id>/<nickname>/', views.index, name='index'),
    # path('', views.index, name='index'),
    # path('form', views.form, name='form'),
    # path('next', views.next, name='next'),
    # path('test', views.test, name='test'),
    path('',HelloView.as_view(),name="index")
]