from django.db import models
# Create your models here.
  

class Admin(models.Model):
    userID      = models.CharField(max_length=30,primary_key=True)
    email       = models.CharField(max_length=30)
    name        = models.CharField(max_length=50)
    contact     = models.CharField(max_length=15)
    department  = models.CharField(max_length=30)
    password    = models.CharField(max_length=50)

    def __str__(self):
        return self.userID 


class NodalOfficer(models.Model):
    userID      = models.CharField(max_length=30,primary_key=True)
    email       = models.CharField(max_length=30)
    name        = models.CharField(max_length=50)
    contact     = models.CharField(max_length=15)
    department  = models.CharField(max_length=30)
    password    = models.CharField(max_length=50)

    def __str__(self):
        return self.userID 
    
