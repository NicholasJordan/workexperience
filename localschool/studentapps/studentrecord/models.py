from django.db import models

# Create your models here.

class Studentinput(models.Model):
        #student = models.ForeignKey()
        work_detail_date = models.DateField()
        Work_detail = models.CharField(max_length=500)
