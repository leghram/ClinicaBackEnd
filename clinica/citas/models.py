from tkinter import CASCADE
from django.db import models
from autorizacion.models import Usuario

class Cita(models.Model):

    id = models.AutoField(primary_key=True, unique=True)
    fecha = models.DateTimeField()
    usuarioId = models.ForeignKey(to=Usuario, related_name="citas", db_column='usuario_id', on_delete=models.CASCADE)

    class Meta:
        db_table = "citas"
        ordering = ['fecha']



