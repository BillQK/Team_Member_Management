from django.db import models

# Create your models here.

# Member Models 
class Member(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100, default=None)
    Email = models.CharField(max_length=200, default= None)
    PhoneNumber = models.CharField(unique=True, max_length=200, default=None)
    admin = models.BooleanField(default=False)
    def __str__(self):
        return self.FirstName