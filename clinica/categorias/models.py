from django.db import models


class Categoria(models.Model):

    opciones = [('cliente','cliente'),('doctor','doctor')]

    id= models.AutoField(primary_key=True, unique=True)
    tipousuario = models.CharField(db_column='tipo_usuario',choices=opciones, max_length=10, default='cliente')

    class Meta:
        db_table='categorias'




