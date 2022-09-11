from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True, blank=True)
    usertype = models.CharField(choices = [('d','doctor'), ('p','patient')], max_length=1)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient')
    dob = models.DateField(null=True, blank=True)
    contact = models.CharField(null=True, blank=True, max_length=100)
    def __str__(self):
        return self.user.name


class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor')
    deg = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.user.name


class Appointments(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    app_time = models.DateTimeField()
    diognoses = models.TextField(max_length=1000)
    prescriptions = models.TextField(max_length=250)


    class Meta:
        unique_together = ('doctor', 'patient', 'app_time')

    def __str__(self):
        st = (str(self.doctor.user.name)+str(self.patient.user.name)).lower().strip()
        return st
