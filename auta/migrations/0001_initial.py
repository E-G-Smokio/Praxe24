# Generated by Django 5.0.6 on 2024-05-15 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AutaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('znacka', models.CharField(max_length=30)),
                ('model', models.CharField(max_length=40)),
                ('rok', models.IntegerField()),
                ('popis', models.TextField(blank=True, null=True)),
                ('datumPridani', models.DateField(auto_now=True)),
            ],
        ),
    ]