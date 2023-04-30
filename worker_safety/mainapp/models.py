from django.db import models

# Create your models here.
class WorkerDetails(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    age = models.CharField(max_length=3 , blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    phn_num = models.CharField(max_length=13, blank=True, null=True)
    medical_history = models.TextField(max_length=2000, blank=True, null=True)
    safety_breach = models.IntegerField(blank=True, null= True)

