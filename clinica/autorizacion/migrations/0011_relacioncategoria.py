# Generated by Django 4.1 on 2022-08-20 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autorizacion', '0010_relacioncategoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='categoriaid',
        ),
        migrations.AddField(
            model_name='usuario',
            name='categoria',
            field=models.CharField(choices=[('cliente', 'cliente'), ('doctor', 'doctor')], default='cliente', max_length=10),
        ),
    ]