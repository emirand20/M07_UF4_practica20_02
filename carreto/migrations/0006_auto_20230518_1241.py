# Generated by Django 4.1.6 on 2023-05-18 10:41

from django.db import migrations

from carreto import models


class Migration(migrations.Migration):

    dependencies = [
        ('carreto', '0005_auto_20230518_1239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carreto',
            name='idCarreto',
        ),
        migrations.RemoveField(
            model_name='carreto',
            name='nombreCarreto',
        ),
    ]
