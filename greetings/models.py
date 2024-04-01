from django.db import models

class Doctor(models.Model):
    doctor_poster = models.URLField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=255)
    specialties = models.CharField(max_length=255)
    mobile_number = models.IntegerField()
    available = models.BooleanField(default=True)
    
