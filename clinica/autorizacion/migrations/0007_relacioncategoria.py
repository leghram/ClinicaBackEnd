# Generated by Django 4.1 on 2022-08-19 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autorizacion', '0006_relacioncategoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='apellido',
            field=models.CharField(max_length=70),
        ),
    ]
