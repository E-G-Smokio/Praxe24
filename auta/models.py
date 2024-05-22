from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
import uuid

# Create your models here.

ZNACKY_AUT = (
    ("Opel", "OPL"),
    ("Skoda", "SKD"),
    ("BMW", "BMW"),
    ("Ford", "FRD"),
    ("Nissan", "NSN"),
    ("Honda", "HND"),
    ("Volkswagen", "VW"),
    ("Porsche", "PRS"),
)


class AutaModel(models.Model):
    znacka = models.CharField(max_length=10, choices=ZNACKY_AUT, default="Vyber")
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    model = models.CharField(max_length=40)
    popis = models.TextField(null=True, blank=True)
    auto_oblazek = models.ImageField(
        upload_to="images/",
        height_field=None,
        width_field=None,
        max_length=None,
        default="",
    )
    vypujceno = models.BooleanField(default=False)

    def __str__(self):
        if Vypujcka == True:
            return self.znacka + ", " + self.model + " AKTUÁLNĚ VYPŮJČENO"
        else:
            return self.znacka + ", " + self.model + " DOSTUPNÉ"

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.id})


class Zakaznik(models.Model):
    email = models.CharField(max_length=100, default="")
    tel_cislo = models.CharField(max_length=20, default="")
    jmeno_zakaznika = models.CharField(max_length=30)
    prijmeni_zakaznika = models.CharField(max_length=30)
    rc_zakaznika = models.CharField(max_length=10, primary_key=True)
    # Vypujcky = models.ForeignKey(Vypujcka, on_delete=models.CASCADE)

    def __str__(self):
        return self.rc_zakaznika


class Vypujcka(models.Model):
    id_vypujcky = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    id_zakaznika = models.ForeignKey(Zakaznik, on_delete=models.CASCADE)
    vypujcene_vozidlo = models.ForeignKey(AutaModel, on_delete=models.CASCADE)
    odkdy = models.DateTimeField(auto_now=True)
    dokdy = models.DateTimeField()
    stav_tach_zacatek = models.IntegerField()
    stav_tach_konec = models.IntegerField(blank=True, null=True)
    stav_nadrze = models.IntegerField()
    ukonceno = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return str(self.id_vypujcky)
