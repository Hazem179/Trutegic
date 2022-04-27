from django.utils import timezone
from django.db import models

# Create your models here.


MEETING = (('online', 'Online'),
           ('offline', 'Offline'))

DAYS_OF_WEEK = (
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
)

CONSULTATIONS = (('marketing_plan', 'Marketing plan'),
                 ('business_plan', 'Business plan'),
                 ('social_media_plan', 'Social media plan'),
                 ('hiring_techniques', 'Hiring techniques'),
                 ('software_developing', 'Software developing'),
                 ('startup_consultation', 'Startup Consultation'),
                 ('get_technical_partnership', 'Get technical partnership'))

SERVICES = (('marketing', 'Marketing'),
            ('software_development', 'Software Development'),
            ('become_a_partner','Become A Partner'))


class AdvisorType(models.Model):
    adv_type = models.CharField(choices=CONSULTATIONS, max_length=32)

    def __str__(self):
        return self.adv_type


class Customer(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=21)
    email = models.EmailField()
    consultation = models.CharField(max_length=32, choices=SERVICES)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Advisor(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    type = models.ManyToManyField(AdvisorType, related_name='types')

    def __str__(self):
        return self.name


class AvailableTimes(models.Model):
    day = models.CharField(max_length=10,choices=DAYS_OF_WEEK,null=True)
    from_hour = models.TimeField(null=True)
    to_hour = models.TimeField(null=True)
    advisor = models.ForeignKey(Advisor, on_delete=models.CASCADE, related_name='times')
    state = models.CharField(choices=(('available', 'Available'),
                                      ('not available', 'Not Available')), max_length=16, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.day


class Consultation(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    consultation = models.CharField(max_length=150, choices=CONSULTATIONS)
    message = models.TextField()
    reservation = models.DateTimeField()
    meeting = models.CharField(choices=MEETING, max_length=12)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    advisor = models.ForeignKey(Advisor, on_delete=models.CASCADE)
    time = models.ForeignKey(AvailableTimes, on_delete=models.CASCADE)
