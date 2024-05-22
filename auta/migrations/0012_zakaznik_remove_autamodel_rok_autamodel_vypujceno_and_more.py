# Generated by Django 5.0.6 on 2024-05-20 18:52

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auta", "0011_remove_autamodel_odkazoblazku_autamodel_autooblazek"),
    ]

    operations = [
        migrations.CreateModel(
            name="Zakaznik",
            fields=[
                ("jmenoZakaznika", models.CharField(max_length=30)),
                ("prijmeniZakaznika", models.CharField(max_length=30)),
                (
                    "rcZakaznika",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="autamodel",
            name="rok",
        ),
        migrations.AddField(
            model_name="autamodel",
            name="Vypujceno",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="autamodel",
            name="znacka",
            field=models.CharField(
                choices=[
                    ("Opel", "OPL"),
                    ("Skoda", "SKD"),
                    ("BMW", "BMW"),
                    ("Ford", "FRD"),
                    ("Nissan", "NSN"),
                    ("Honda", "HND"),
                    ("Volkswagen", "VW"),
                    ("Porsche", "PRS"),
                ],
                default="Vyber",
                max_length=10,
            ),
        ),
        migrations.CreateModel(
            name="Vypujcka",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "idVypujcky",
                    models.UUIDField(default="", unique=True, verbose_name=uuid.uuid4),
                ),
                ("Odkdy", models.DateTimeField(auto_now=True)),
                ("Dokdy", models.DateTimeField()),
                ("stavTachZacatek", models.IntegerField()),
                ("stavTachKonec", models.IntegerField()),
                ("stavNadrze", models.IntegerField()),
                (
                    "vypujceneVozidlo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="auta.autamodel"
                    ),
                ),
                (
                    "idZakaznika",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="auta.zakaznik"
                    ),
                ),
            ],
        ),
    ]
