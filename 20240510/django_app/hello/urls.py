from django.urls import path
# from .views import HelloView
from . import views
from .views import FriendList, FriendDetail

urlpatterns = [
    path('find',views.find, name="find"),
    # path('<int:id>/<nickname>/', views.index, name='index'),
    path('', views.index, name='index'),
    # path('form', views.form, name='form'),
    # path('next', views.next, name='next'),
    # path('test', views.test, name='test'),
    # path('',HelloView.as_view(),name="index")
    path('create',views.create,name="create"),
    path('edit/<int:id>',views.edit,name="edit"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('list',FriendList.as_view(),name="list"),
    path('detail/<int:pk>',FriendDetail.as_view(),name="detail"),
    path('check',views.check,name="check")
]