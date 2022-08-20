# Generated by Django 4.1 on 2022-08-20 04:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('especialidades', '0002_creacionModeloEspecialidad'),
        ('citas', '0004_relacioncategoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cita',
            name='especialidadId',
            field=models.ForeignKey(db_column='especialidad_id', on_delete=django.db.models.deletion.CASCADE, related_name='relacionEspecialidad', to='especialidades.especialidad'),
        ),
    ]