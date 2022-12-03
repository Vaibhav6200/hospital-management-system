from django.db import models


class RegisteredUser(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(unique=True,blank=False)
    password = models.CharField(max_length=6, blank=False)
    phone_number = models.IntegerField()
    DOB = models.DateField(blank=False)
    address = models.TextField(max_length=100)
    gender = models.CharField(max_length=12)

    def __str__(self):
        return str(self.first_name +  self.last_name)
