from django.db import models



# Create your models here.
class Student(models.Model):
    #Name of the student
    student = models.CharField(max_length=200)
    #Form group choices variables
    C = "CAMPION"
    L = "LINE"
    M = "MAYNE"
    S = "STONE"
    #Form group choices
    FORM_GROUP_CHOICES = (
        (C,'Campion'),
        (L, 'Line'),
        (M, 'Mayne'),
        (S, 'Stone'),
    )
    #Form group field
    form_group = models.CharField(max_length=7, choices=FORM_GROUP_CHOICES, default=C,)
    #Work experience details
    location = models.CharField(max_length=200)
    """details_entered = #wait for student details app to be added"""
    company_name = models.CharField(max_length=200, default='Not entered')
    company_contact = models.CharField(max_length=200, default='eg. Helen Stephane')
    company_phone = models.CharField(max_length=200, default='Not entered')
    company_email = models.EmailField(max_length=200, default='Not entered')

    def __str__(self):
        return self.student
