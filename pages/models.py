from django.utils import timezone
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


MEETING = (('online','Online'),
           ('offline','Offline'))

DAYS_OF_WEEK = (
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
)



CONSULTATIONS = (('1', 'Marketing plan'),
                 ('2', 'Business plan'),
                 ('3', 'Social media plan'),
                 ('4', 'Hiring techniques'),
                 ('5', 'Software developing'),
                 ('6', 'Startup Consultation'),
                 ('7', 'Get technical partnership'))

HOURS = (('1:00-2:00pm','1:00-2:00pm'),
         ('2:00-3:00pm','2:00-3:00pm'),
         ('3:00-4:00pm','3:00-4:00pm'))


class Customer(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    consultation = models.CharField(max_length=150,choices=CONSULTATIONS)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)



    def __str__(self):
       return self.name





class Advisor(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    type = models.CharField(max_length=150,choices=CONSULTATIONS)


    def __str__(self):
        return self.name


class AvailableTimes(models.Model):
    day = models.DateField(null=True)
    from_hour = models.TimeField(null=True)
    to_hour = models.TimeField(null=True)
    advisor = models.ForeignKey(Advisor,on_delete=models.CASCADE,related_name='times')
    state = models.CharField(choices=(('available','Available'),
                                      ('not available','Not Available')),max_length=16,null=True)
    created_at = models.DateTimeField(default=timezone.now)


    @property
    def week_day(self):
        return f'{self.day.strftime("%A")}'


    def __str__(self):
        return f'{self.day.strftime("%A")}'





class Consultation(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    consultation = models.CharField(max_length=150, choices=CONSULTATIONS)
    message = models.TextField()
    reservation =  models.DateTimeField()
    meeting = models.CharField(choices=MEETING,max_length=12)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        self.name



class Reservation(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    advisor =  models.ForeignKey(Advisor,on_delete=models.CASCADE)
    time = models.ForeignKey(AvailableTimes,on_delete=models.CASCADE)