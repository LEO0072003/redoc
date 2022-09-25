from django.contrib import messages
from django.shortcuts import render, redirect
from django.forms import HiddenInput

from rec.forms import (MyUserCreation,
                        DoctorCreation,
                        PatientCreation,
                        )

from .models import (Patient,
                    Doctor,
                    User,
                    Appointments)

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    doctor = Doctor.objects.all()[0:5]
    context = {'doctor': doctor}
    return render(request, 'rec/home.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user= User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request=request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'rec/login.html', {'page':'login'})

def logoutPage(request):
    logout(request)
    return redirect('home')

def registerUser(request):
    form = None

    if request.method == 'POST':
        print(request.POST)
        valid = False

        if 'usertype' in request.POST:
            # 1st form submit

            form = MyUserCreation(request.POST)
            if form.is_valid:
                valid = True
                user = form.save(commit=False)
                user.save()
                login(request, user)

                # Get 2nd form for load
                if user.usertype == 'p':
                    page = 'patient'
                    form = PatientCreation(initial={'user':user})
                    form.fields['user'].widget = HiddenInput()
                elif user.usertype== 'd':
                    page = 'doctor'
                    form = DoctorCreation(initial={'user':user})

        else:
            # 2nd form submit

            if 'dob_year' in request.POST:
                form = PatientCreation(request.POST)
                if form.is_valid:
                    form.save()
                    valid = True

            elif 'deg' in request.POST:
                form = DoctorCreation(request.POST)
                if form.is_valid:
                    form.save()
                    valid = True

            if valid:
                # form sequence done
                return redirect('home')

        if not valid:
            # a form failed somewhere
            # print(form.errors)
            messages.error(request, 'Error occured')


    if form == None:
        page = 'general'
        form = MyUserCreation()

    context = {'form':form, 'page':page}
    return render(request, 'rec/register_user.html', context )


# def registerUser(request):
#     ucf = MyUserCreation()
#     ucf.fields['usertype'].widget = HiddenInput()
#     form = None
#     if request.method == 'POST':
#         u_t = request.POST.get('usertype')
#         if u_t=='':
#             redirect('rec/register_user.html')
#             messages.error(request, 'Please select an Usertype')

#         elif u_t=='doctor':
#             # user = Doctor.create_dr()
#             form = DoctorCreation()

#             # form.initial = {'user':user}
#             # ucf.fields['user'].widget = HiddenInput()

#             ucf.initial = {'usertype':'d'}
#             context = {'form':form, 'ucf':ucf}
#             return render(request,'rec/register_user.html',context)

#         else:
#             form = PatientCreation()
#             ucf.initial = {'usertype':'p'}
#             context = {'form':form, 'ucf':ucf}
#             return render(request,'rec/register_user.html',context)


#     return render(request,'rec/register_user.html')

def userProfile(request, pk):
    user = User.objects.get(id=pk)
    context = {'user':user}
    return render(request, 'rec/user_profile.html', context)

@login_required(login_url='login')
def appointmentDetails(request, pk):

    context = {}
    print(request.user.usertype)
    if request.user.usertype == 'p':
        appointments = Appointments.objects.filter(patient=request.user.id)

    return render(request, 'rec/appointment.html', context)
