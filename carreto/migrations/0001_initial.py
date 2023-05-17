# Generated by Django 3.2.18 on 2023-05-17 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0002_auto_20230517_1932'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carreto',
            fields=[
                ('id', models.AutoField(auto_created=True, default='cb95a3b436064e7fbb99f35839422ff1', primary_key=True, serialize=False)),
                ('nombreCarreto', models.CharField(default=None, max_length=50)),
                ('isBuy', models.BooleanField(default=False)),
                ('productos', models.ManyToManyField(to='catalog.Producto')),
            ],
        ),
    ]
