# Generated by Django 3.2.18 on 2023-05-02 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio')),
            ],
        ),
    ]
