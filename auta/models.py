from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# Create your models here.



class Znacky(models.Model):
    class TypeChoices(models.TextChoices):
        OPEL = 'OPL', 'Opel'
        SKODA = 'SKD', 'Skoda'
        FORD = 'FRD', 'Ford'
        BMW = 'BMW', 'Bmw'
        NISSAN = 'NSN', 'Nissan'
        HONDA = 'HND', 'Honda'  

class AutaModel(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    model = models.CharField(max_length=40)
    rok = models.IntegerField()
    popis = models.TextField(null=True, blank=True)
    datumPridani = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.model