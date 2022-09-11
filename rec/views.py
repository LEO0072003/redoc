from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Patient, Doctor, User, Appointments
from django.contrib.auth import login, authenticate, logout

# Create your views here.

def home(request):
    doctor = Doctor.objects.all()[0:5]
    context = {'doctor': doctor}
    return render(request, 'rec/home.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    
    try:
        user= User.objects.get('username')
    except:
        messages.error(request, 'User does not exist')
    
    user = authenticate(request, username='username', passwword='password')

    if user is not None:
        login(request, user)
        return redirect(request,'home')

    return render(request, 'rec/login.html', {'page':'login'})