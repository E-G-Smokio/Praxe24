from django.db import models

# Create your models here.

class AutaModel(models.Model):
    znacka = models.CharField(max_length=30)
    model = models.CharField(max_length=40)
    rok = models.IntegerField()
    popis = models.TextField(null=True, blank=True)
    datumPridani = models.DateField(auto_now=True)

    def __str__(self):
        return self.znacka