from django.db import models

class OrAdmin(models.Model):
    username = models.CharField(max_length=150, default='', unique=True) 
    email = models.CharField(max_length=254, default='', unique=True)   
    password1 = models.CharField(max_length=128, default='') 
    password2 = models.CharField(max_length=128, default='')

    

    def __str__(self):
        return self.username


class Tn1MME(models.Model):
    date = models.CharField(max_length=150, default='', unique=True)
    attach2g3g = models.DecimalField(max_digits=10, decimal_places=2)
    attach4g = models.DecimalField(max_digits=10, decimal_places=2)
    pdpact2g3g = models.DecimalField(max_digits=10, decimal_places=2)
    attach3g = models.DecimalField(max_digits=10, decimal_places=2)    
    sau2g3g = models.BigIntegerField()
    sau4g = models.BigIntegerField()
    pdp = models.BigIntegerField()
    bearer = models.BigIntegerField()

class Tn2MME(models.Model):
    date = models.CharField(max_length=150, default='', unique=True)
    attach2g3g = models.DecimalField(max_digits=10, decimal_places=2)
    attach4g = models.DecimalField(max_digits=10, decimal_places=2)
    pdpact2g3g = models.DecimalField(max_digits=10, decimal_places=2)
    attach3g = models.DecimalField(max_digits=10, decimal_places=2)
    sau2g3g = models.BigIntegerField()
    sau4g = models.BigIntegerField()
    pdp = models.BigIntegerField()
    bearer = models.BigIntegerField()

class SoMME(models.Model):
    date = models.CharField(max_length=150, default='', unique=True)
    attach2g3g = models.DecimalField(max_digits=10, decimal_places=2)
    attach4g = models.DecimalField(max_digits=10, decimal_places=2)
    pdpact2g3g = models.DecimalField(max_digits=10, decimal_places=2)
    attach3g = models.DecimalField(max_digits=10, decimal_places=2)
    sau2g3g = models.BigIntegerField()
    sau4g = models.BigIntegerField()
    pdp = models.BigIntegerField()
    bearer = models.BigIntegerField()
    
class Int(models.Model):
    date = models.CharField(max_length=150, default='', unique=True)
    bhTN1 = models.DecimalField(max_digits=10, decimal_places=2)
    bhTN2 = models.DecimalField(max_digits=10, decimal_places=2)
    bhSO = models.DecimalField(max_digits=10, decimal_places=2)



