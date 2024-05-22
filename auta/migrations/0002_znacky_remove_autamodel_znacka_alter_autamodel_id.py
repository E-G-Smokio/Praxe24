# Generated by Django 5.0.6 on 2024-05-16 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auta", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Znacky",
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
            ],
        ),
        migrations.RemoveField(
            model_name="autamodel",
            name="znacka",
        ),
        migrations.AlterField(
            model_name="autamodel",
            name="id",
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]
