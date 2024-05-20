from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
# Create your models here.

ZnackyAut = (
    ('Opel', 'OPL'),
    ('Skoda', 'SKD'),
    ('BMW', 'BMW'),
    ('Ford', 'FRD'),
    ('Nissan', 'NSN'),
    ('Honda', 'HND'),
)
        

class AutaModel(models.Model):
    znacka = models.CharField(max_length=10, choices=ZnackyAut, default='Vyber') 
    id = models.PositiveIntegerField(primary_key=True, null=False, unique=True, auto_created=True)
    model = models.CharField(max_length=40)
    rok = models.IntegerField()
    popis = models.TextField(null=True, blank=True)
    datumPridani = models.DateField()

    def __str__(self):
        return self.znacka
    
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.id})
    