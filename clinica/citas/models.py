from django.db import models

class Cita(models.Model):

    id = models.AutoField(primary_key=True, unique=True)
    fecha = models.DateTimeField()


    class Meta:
        db_table = "citas"
        ordering = ['fecha']



