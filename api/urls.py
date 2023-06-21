from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('',views.Home,name='home'),
    path('users/',views.Users,name='alluser'),
    path('user/<str:pk>/',views.User,name='particularUser'),
    path('new/',views.createUser,name='newUser'),
    path('update/<str:pk>/',views.updateUser,name='update'),
    path('delete/<str:pk>/',views.deleteUser,name='delete'),
]
