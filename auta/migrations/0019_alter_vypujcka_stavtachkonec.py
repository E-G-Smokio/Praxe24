# Generated by Django 5.0.6 on 2024-05-20 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auta", "0018_alter_vypujcka_idvypujcky"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vypujcka",
            name="stavTachKonec",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
