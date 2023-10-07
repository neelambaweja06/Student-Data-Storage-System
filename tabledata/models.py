from django.db import models

# Create your models here.
class reginfo(models.Model):
    regno=models.CharField(max_length=50)
    name=models.CharField(max_length=20)
    fname=models.CharField(max_length=20)
    mname=models.CharField(max_length=20)
    phone=models.CharField(max_length=15)
    address=models.CharField(max_length=50)
    city=models.CharField(max_length=20)
    gender=models.CharField(max_length=10)
    course=models.CharField(max_length=50)
    btime=models.CharField(max_length=20)
    photo=models.CharField(max_length=50)