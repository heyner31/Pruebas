from django.db import models

# Create your models here.

class Dogs(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    type_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dogs'

class Types(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'types'


class Ingredientes(models.Model):
    id_in = models.AutoField(db_column='id_In', primary_key=True)  # Field name made lowercase.
    nombre_in = models.CharField(db_column='Nombre_in', max_length=100, blank=True, null=True)  # Field name made lowercase.
    img_in = models.CharField(max_length=1500, blank=True, null=True)
    tipo = models.CharField(db_column='Tipo', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Ingredientes'


class Recetas(models.Model):
    id_re = models.AutoField(primary_key=True)
    nombre_re = models.CharField(db_column='Nombre_re', max_length=500, blank=True, null=True)  # Field name made lowercase.
    procedimiento_re = models.CharField(db_column='Procedimiento_re', max_length=1500, blank=True, null=True)  # Field name made lowercase.
    calorias_re = models.IntegerField(db_column='Calorias_re', blank=True, null=True)  # Field name made lowercase.
    img_re = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Recetas'