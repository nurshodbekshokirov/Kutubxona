from django.db import models
from django.db.models import Sum,Max,Avg,Count,Min
import random



class Muallif(models.Model):
    Jins= [
        ('Erkak','Erkak'),
        ('Ayol','Ayol')
    ]
    ism = models.CharField(max_length=50)
    tugilgan_yil = models.DateField(null=False)
    tirik = models.BooleanField()
    kitob_soni = models.PositiveSmallIntegerField()
    jins = models.CharField(max_length=30, choices=Jins)

    def __str__(self):
        return f"{self.ism}"
class Admin(models.Model):
    ism = models.CharField(max_length=50)
    ish_vaqti = models.CharField(max_length=30)
    def __str__(self):
        return self.ism
class kitob(models.Model):
    nom = models.CharField(max_length=50)
    sahifa = models.SmallIntegerField()
    janr = models.CharField(max_length=30,choices=[('Badiiy','Badiiy'),('Ilmiy','Ilmiy'),('Hujjatli','Hujjatli')])
    muallif = models.ForeignKey(Muallif,on_delete=models.CASCADE)
    def __str__(self):
        return self.nom
class Talaba(models.Model):
    ism = models.CharField(max_length=50)
    kitob_soni = models.PositiveSmallIntegerField(default=0)
    kurs = models.PositiveSmallIntegerField()
    bitiruvchi = models.BooleanField(default=False)
    def __str__(self):
        return self.ism
class Record(models.Model):
    talaba = models.ForeignKey(Talaba,on_delete=models.CASCADE)
    kitob = models.ForeignKey(kitob,on_delete=models.CASCADE)
    admin = models.ForeignKey(Admin,on_delete=models.CASCADE)
    olingan_sana = models.DateField()
    qaytardi = models.BooleanField(default=False)
    qaytargan_sana = models.DateField(blank=True)




