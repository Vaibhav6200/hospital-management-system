from hospitalAPP.models import Departments, Doctors
from django.db.models.expressions import OrderBy
from django.shortcuts import render
from django.db import models

class Booking(models.Model):
    full_name = models.CharField(max_length=25,blank=False)
    profile_photo = models.ImageField(upload_to="bookedprofiles")
    contact_number = models.CharField(max_length=12, blank=False)
    booking_date = models.DateField(blank=False)
    booking_time = models.TimeField(blank=True)
    deasease = models.CharField(max_length=50,blank=False)
    doc_name = models.CharField(max_length=12, blank=False)
    dep_name = models.CharField(max_length=12, blank=False)

    def __str__(self):
        return self.full_name
