# Generated by Django 5.0.6 on 2024-05-20 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auta', '0007_autamodel_odkazoblazku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autamodel',
            name='id',
            field=models.UUIDField(primary_key=True, serialize=False, unique=True),
        ),
    ]
