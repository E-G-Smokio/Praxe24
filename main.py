from django.db import models

class auto(models.Model):
    Znacka = models.CharField(max_length=15)
    model_votu = models.CharField(max_length=20)
    rok_vyroby = models.IntegerField()


print(auto.Znacka)