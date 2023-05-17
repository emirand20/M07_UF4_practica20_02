# Generated by Django 3.2.18 on 2023-05-17 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=6)),
                ('caducidad', models.DateField(default='2023-12-31')),
                ('descripcion', models.TextField()),
                ('codigo', models.CharField(default='af50a8', max_length=6, unique=True)),
                ('codigoDeBarras', models.CharField(default='cb0ea3f1601e426d8ab3ecdd95322012', editable=False, max_length=32, unique=True)),
            ],
        ),
    ]
