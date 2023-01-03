from django.db import models

# Create your models here.
class solucionario(models.Model):
    id_ejercicio = models.CharField(max_length = 200, verbose_name = "id del ejercicio")

    def __str__(self):
        return self.id_ejercicio

    class Meta:
        verbose_name = 'solucionario'
        db_table = 'solucionario_teclado'
        ordering = ['id']

class enunciado_solucion(models.Model):
    id_ejercicio = models.ForeignKey(solucionario, on_delete=models.CASCADE)
    enunciado = models.TextField(blank = True, verbose_name = "enunciado")
    solucionario = models.TextField(blank = True, verbose_name = "solucionario")

    def __str__(self):
        return self.enunciado

    class Meta:
        verbose_name = 'Enunciado solucion'
        db_table = 'Enunciado solucion tabla'
        ordering = ['id']

