# Generated by Django 5.0.6 on 2024-05-20 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auta", "0005_alter_autamodel_id_alter_autamodel_znacka"),
    ]

    operations = [
        migrations.AlterField(
            model_name="autamodel",
            name="datumPridani",
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="autamodel",
            name="id",
            field=models.PositiveIntegerField(
                primary_key=True, serialize=False, unique=True
            ),
        ),
    ]
