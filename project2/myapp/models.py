from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    email = models.EmailField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=20)
    otp = models.CharField(max_length=20,default=None)

    def __repr__(self):
       return "<CustomUser(email='%s',first_name='%s',last_name='%s',gender='%s',phone_number='%s')>" % (
                            self.email,self.first_name,self.last_name,self.gender,self.phone_number)