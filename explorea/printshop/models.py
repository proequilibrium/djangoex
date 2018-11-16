from django.db import models

# Create your models here.
class Paper(models.Model):
    name = models.CharField(max_length=200)
    sizeWidth = models.IntegerField()
    sizeHeight = models.IntegerField()
    gsm = models.IntegerField()
    costPerKilo=models.DecimalField(max_digits=3,decimal_places=2)
    papertype=models.CharField(max_length=50)

class Customer(models.Model):
    name = models.IntegerField()
    ICO = models.BigIntegerField()
    tel = models.CharField(max_length = 13)
    spec = models.CharField(max_length=200)

class Job(models.Model):
    jobID = models.CharField(max_length=200)
    term = models.DateField()
    priceNet = models.BigIntegerField()
    spec = models.CharField()
    cooperation = models.CharField()
    status = models.CharField(max_length = 15)

class Work(models.Model):
    name = models.CharField(max_length=500)
    costPerHour = models.IntegerField()

#class worker(models.Model):

#class task(models.Model)
#    taskTicket =
#    idjob
#    ammount
#    taskid
