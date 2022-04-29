from django.db import models
from django.conf import settings


# Create your models here.
class Student(models.Model):
    MAJOR_CHOICES = [
        ('finance', 'Finance'),
        ('engineering', 'Engineering'),
        ('accounting','Accounting'),
        ('marketing','Marketing'),
        ('real estate','Real Estate'),
        ('it','Information Technology Management'),
        ('undecided','undecided')
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, 
                             related_name='student')
    name = models.CharField(max_length=200)
    major = models.CharField(max_length=20,choices= MAJOR_CHOICES, default = 'undecided')
    