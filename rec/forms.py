from django import forms
from .models import (Doctor,
                    User,
                    Patient,
                    Appointments
                    )
from django.contrib.auth.forms import UserCreationForm

class MyUserCreation(UserCreationForm):
    class Meta:
        model = User
        fields = ['name','username','usertype']



class DoctorCreation(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['user','deg']

class PatientCreation(forms.ModelForm):
    dob = forms.DateField(widget=forms.SelectDateWidget(years=range(1960,2022)))
    class Meta:
        model = Patient
        fields = ['user','contact','dob']
        # widgets = {
        #             'dob': forms.DateField(widget=forms.SelectDateWidget(years=range(1960,2022))),
        #             }




class AppointmentBookForm(forms.ModelForm):
    class Meta:
        model = Appointments
        fields = ['doctor','app_time']

