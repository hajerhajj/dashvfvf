from django.db import models

class OrAdmin(models.Model):
    username = models.CharField(max_length=150, default='') 
    email = models.CharField(max_length=254, default='')   
    password1 = models.CharField(max_length=128, default='') 
    password2 = models.CharField(max_length=128, default='')

    def __str__(self):
        return self.username