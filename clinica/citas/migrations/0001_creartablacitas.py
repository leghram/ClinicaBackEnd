# Generated by Django 4.1 on 2022-08-19 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('fecha', models.DateTimeField()),
            ],
            options={
                'db_table': 'clinica',
                'ordering': ['fecha'],
            },
        ),
    ]
