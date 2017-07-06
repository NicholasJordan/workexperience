from django.db import models

# Create your models here.

#Model for formgroup Campion and their students
class Campion(models.Model):
    name = models.CharField(max_length=200)
    #formgroup = models.CharField
