from django.db import models
from accounts.models import Patients

# Create your models here.

class Appointment(models.Model):
    patient = models.ForeignKey(Patients, null = True, blank = True, on_delete = models.SET_NULL)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    request = models.TextField(blank=True)
    sent_date = models.DateField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    do_date = models.DateField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.first_name
