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
    pdpactnbr2g = models.BigIntegerField()
    pdpactnbr3g = models.BigIntegerField()


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
    pdpactnbr2g = models.BigIntegerField()
    pdpactnbr3g = models.BigIntegerField()

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
    pdpactnbr2g = models.BigIntegerField()
    pdpactnbr3g = models.BigIntegerField()
    
class Int(models.Model):
    date = models.CharField(max_length=150, default='', unique=True)
    bhTN1 = models.DecimalField(max_digits=10, decimal_places=2)
    bhTN2 = models.DecimalField(max_digits=10, decimal_places=2)
    bhSO = models.DecimalField(max_digits=10, decimal_places=2)
    bhGlobal = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.bhTN1 is not None and self.bhTN2 is not None and self.bhSO is not None:
            self.bhGlobal = (self.bhTN1 + self.bhTN2 + self.bhSO) / 3
        else:
            self.bhGlobal = None
        
        super().save(*args, **kwargs)


class Tn1EPG(models.Model):
    date = models.CharField(max_length=150, default='', unique=True)
    avg16 = models.IntegerField()
    peak16 = models.IntegerField()
    avg4 = models.IntegerField()
    peak4 = models.IntegerField()
    avg5 = models.IntegerField()
    peak5 = models.IntegerField()
    avg14 = models.IntegerField()
    peak14 = models.IntegerField()
    avg15 = models.IntegerField()
    peak15 = models.IntegerField()
    avg17 = models.IntegerField()
    peak17 = models.IntegerField()
    avg6 = models.IntegerField()
    peak6 = models.IntegerField()
    actpdpcont = models.BigIntegerField()
    acteps = models.BigIntegerField()
    actsub = models.BigIntegerField()  


class SOEPG(models.Model):
    date = models.CharField(max_length=150, default='', unique=True)
    avg29 = models.IntegerField()
    peak29 = models.IntegerField()
    avg30 = models.IntegerField()
    peak30 = models.IntegerField()
    avg1 = models.IntegerField()
    peak1 = models.IntegerField()
    avg2 = models.IntegerField()
    peak2 = models.IntegerField()
    avg3 = models.IntegerField()
    peak3 = models.IntegerField()
    avg4 = models.IntegerField()
    peak4 = models.IntegerField()
    avg5 = models.IntegerField()
    peak5 = models.IntegerField()
    avg6 = models.IntegerField()
    peak6 = models.IntegerField()
    actpdpcont = models.BigIntegerField()
    acteps = models.BigIntegerField()
    actsub = models.BigIntegerField() 


class TN2VEPG(models.Model):
    date = models.CharField(max_length=150, default='', unique=True)
    avg29 = models.IntegerField()
    peak29 = models.IntegerField()
    avg30 = models.IntegerField()
    peak30 = models.IntegerField()
    avg1 = models.IntegerField()
    peak1 = models.IntegerField()
    avg10 = models.IntegerField()
    peak10 = models.IntegerField()
    avg11 = models.IntegerField()
    peak11 = models.IntegerField()
    avg12 = models.IntegerField()
    peak12 = models.IntegerField()
    avg2 = models.IntegerField()
    peak2 = models.IntegerField()
    avg3 = models.IntegerField()
    peak3 = models.IntegerField()
    avg4 = models.IntegerField()
    peak4 = models.IntegerField()
    avg5 = models.IntegerField()
    peak5 = models.IntegerField()
    avg6 = models.IntegerField()
    peak6 = models.IntegerField()
    avg7 = models.IntegerField()
    peak7 = models.IntegerField()
    avg8 = models.IntegerField()
    peak8 = models.IntegerField()
    avg9 = models.IntegerField()
    peak9 = models.IntegerField()
    actpdpcont = models.BigIntegerField()
    acteps = models.BigIntegerField()
    actsub = models.BigIntegerField() 