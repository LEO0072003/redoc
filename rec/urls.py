from tkinter import N
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),

    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('register_user/', views.registerUser, name='register'),

    path('user_profile/<str:pk>/', views.userProfile, name='profile'),
    path('appointment/<str:pk>', views.appointmentDetails, name='appointment'),

]
