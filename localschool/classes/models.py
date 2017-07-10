from django.db import models

# Create your models here.

#Model for formgroup Campion and their students.
class Campion(models.Model):
    student = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    """details_entered = #wait for student details app to be added"""
    company_name = models.CharField(max_length=200, default='Not entered')
    company_contact = models.CharField(max_length=200, default='eg. Helen Stephane')
    company_phone = models.CharField(max_length=200, default='Not entered')
    company_email = models.EmailField(max_length=200, default='Not entered')

    class Meta:
        verbose_name_plural = 'Campion'
        ordering = ['student']

    def showname(self):
        def __str__(self):
            return self.student

    def __str__(self):
        return self.student[:50]

#Model for formgroup Line and their students.
class Line(models.Model):
    student = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200, default='Not entered')
    """details_entered = #wait for student details app to be added"""
    company_name = models.CharField(max_length=200, default='Not entered')
    company_contact = models.CharField(max_length=200, default='eg. Helen Stephane')
    company_phone = models.CharField(max_length=200, default='Not entered')
    company_email = models.EmailField(max_length=200, default='Not entered')

    class Meta:
        verbose_name_plural = 'Line'
        ordering = ['student']

    def __str__(self):
        return self.student[:50]

#Model for formgroup Mayne and their students.
class Mayne(models.Model):
    student = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200, default='Not entered')
    """details_entered = #wait for student details app to be added"""
    company_name = models.CharField(max_length=200, default='Not entered')
    company_contact = models.CharField(max_length=200, default='eg. Helen Stephane')
    company_phone = models.CharField(max_length=200, default='Not entered')
    company_email = models.EmailField(max_length=200, default='Not entered')

    class Meta:
        verbose_name_plural = 'Mayne'
        ordering = ['student']

    def __str__(self):
        return self.student[:50]

#Model for formgroup Stone and their students.
class Stone(models.Model):
    student = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200, default='Not entered')
    """details_entered = #wait for student details app to be added"""
    company_name = models.CharField(max_length=200, default='Not entered')
    company_contact = models.CharField(max_length=200, default='eg. Helen Stephane')
    company_phone = models.CharField(max_length=200, default='Not entered')
    company_email = models.EmailField(max_length=200, default='Not entered')

    class Meta:
        verbose_name_plural = 'Stone'
        ordering = ['student']

    def __str__(self):
        return self.student[:50]
