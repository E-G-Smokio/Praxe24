# Generated by Django 5.0.6 on 2024-05-21 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auta", "0019_alter_vypujcka_stavtachkonec"),
    ]

    operations = [
        migrations.RenameField(
            model_name="autamodel",
            old_name="autoOblazek",
            new_name="auto_oblazek",
        ),
        migrations.RenameField(
            model_name="autamodel",
            old_name="Vypujceno",
            new_name="vypujceno",
        ),
        migrations.RenameField(
            model_name="vypujcka",
            old_name="Dokdy",
            new_name="dokdy",
        ),
        migrations.RenameField(
            model_name="vypujcka",
            old_name="idVypujcky",
            new_name="id_vypujcky",
        ),
        migrations.RenameField(
            model_name="vypujcka",
            old_name="idZakaznika",
            new_name="id_zakaznika",
        ),
        migrations.RenameField(
            model_name="vypujcka",
            old_name="Odkdy",
            new_name="odkdy",
        ),
        migrations.RenameField(
            model_name="vypujcka",
            old_name="stavNadrze",
            new_name="stav_nadrze",
        ),
        migrations.RenameField(
            model_name="vypujcka",
            old_name="stavTachKonec",
            new_name="stav_tach_konec",
        ),
        migrations.RenameField(
            model_name="vypujcka",
            old_name="stavTachZacatek",
            new_name="stav_tach_zacatek",
        ),
        migrations.RenameField(
            model_name="vypujcka",
            old_name="Ukonceno",
            new_name="ukonceno",
        ),
        migrations.RenameField(
            model_name="vypujcka",
            old_name="vypujceneVozidlo",
            new_name="vypujcene_vozidlo",
        ),
        migrations.RenameField(
            model_name="zakaznik",
            old_name="jmenoZakaznika",
            new_name="jmeno_zakaznika",
        ),
        migrations.RenameField(
            model_name="zakaznik",
            old_name="prijmeniZakaznika",
            new_name="prijmeni_zakaznika",
        ),
        migrations.RenameField(
            model_name="zakaznik",
            old_name="rcZakaznika",
            new_name="rc_zakaznika",
        ),
        migrations.AddField(
            model_name="zakaznik",
            name="email",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AddField(
            model_name="zakaznik",
            name="tel_cislo",
            field=models.CharField(default="", max_length=20),
        ),
    ]
