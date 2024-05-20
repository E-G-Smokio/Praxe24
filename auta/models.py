from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
import uuid
# Create your models here.

ZnackyAut = (
    ('Opel', 'OPL'),
    ('Skoda', 'SKD'),
    ('BMW', 'BMW'),
    ('Ford', 'FRD'),
    ('Nissan', 'NSN'),
    ('Honda', 'HND'),
    ('Volkswagen', 'VW'),
    ('Porsche', 'PRS')
)
        

class AutaModel(models.Model):
    znacka = models.CharField(max_length=10, choices=ZnackyAut, default='Vyber') 
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    model = models.CharField(max_length=40)
    popis = models.TextField(null=True, blank=True)
    autoOblazek = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=None, default='')
    Vypujceno = models.BooleanField(default=False)

    def __str__(self):
        if Vypujcka == True:
            return self.znacka +', '+ self.model + ' AKTUÁLNĚ VYPŮJČENO'
        else:
            return self.znacka +', '+ self.model + ' DOSTUPNÉ'
    
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.id})

class Zakaznik(models.Model):
    jmenoZakaznika = models.CharField(max_length=30)
    prijmeniZakaznika = models.CharField(max_length=30)
    rcZakaznika = models.CharField(max_length=10, primary_key=True)
    #Vypujcky = models.ForeignKey(Vypujcka, on_delete=models.CASCADE)

    def __str__(self):
        return self.rcZakaznika

class Vypujcka(models.Model):
    idVypujcky = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    idZakaznika = models.ForeignKey(Zakaznik, on_delete=models.CASCADE)
    vypujceneVozidlo = models.ForeignKey(AutaModel, on_delete=models.CASCADE)
    Odkdy = models.DateTimeField(auto_now=True)
    Dokdy = models.DateTimeField()
    stavTachZacatek = models.IntegerField()
    stavTachKonec = models.IntegerField(blank=True, null=True)
    stavNadrze = models.IntegerField()
    Ukonceno = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return str(self.idVypujcky)