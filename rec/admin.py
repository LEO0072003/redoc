from django.contrib import admin
from .models import Patient, User, Appointments, Doctor
# Register your models here.

admin.site.register(Patient)
admin.site.register(User)
admin.site.register(Appointments)
admin.site.register(Doctor)
