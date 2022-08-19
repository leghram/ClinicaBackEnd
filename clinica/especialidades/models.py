from django.db import models

class Especialidad(models.Model):

    id= models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=60)
    descripcion = models.TextField()

    class Meta:
        db_table='especialidades'
