from django.utils import timezone
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Customer(models.Model):
    CONSULTATIONS =(('1','Marketing'),
                    ('2','Software'))
    name = models.CharField(max_length=200)
    phone = PhoneNumberField()
    email = models.EmailField()
    consultation = models.CharField(max_length=150,choices=CONSULTATIONS)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)


    def __str__(self):
       return self.name



class Consultant(models.Model):
    name = ''
    email = ''

