from django.db import models
from autorizacion.models import Usuario
from especialidades.models import Especialidad

class Cita(models.Model):

    id = models.AutoField(primary_key=True, unique=True)
    fecha = models.DateTimeField()
    usuarioId = models.ForeignKey(to=Usuario, related_name="relacionUsuarios", db_column='usuario_id', on_delete=models.CASCADE)
    especialidadId = models.ForeignKey(to=Especialidad, related_name="relacionEspecialidad", db_column='especialidad_id', on_delete=models.CASCADE)

    class Meta:
        db_table = "citas"
        ordering = ['fecha']



