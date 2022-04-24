from django.db import models

# Create your models here.
class Team(models.Model):
    SECTIONS = (('board','Board'),
                ('product design','Product Design'),
                ('backend','Backend'),
                ('frontend','Frontend'),
                ('flutter','Flutter'))
    name = models.CharField(max_length=200,db_index=True)
    title = models.CharField(max_length=100)
    section = models.CharField(max_length=100,choices=SECTIONS,default='board')
    email = models.EmailField() # change to phone number later
    image = models.ImageField(upload_to='team/')
    def __str__(self):
        return self.name

class Advisor(models.Model):
    name = models.CharField(max_length=200,db_index=True)
    title = models.CharField(max_length=100)
    email = models.EmailField()
    image = models.ImageField()

