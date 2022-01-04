from django.db import models


class Aula(models.Model):
    nombre = models.CharField(max_length=50)
    grado = models.CharField(max_length=2)


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    sexo = models.CharField(max_length=20)
    grupo = models.ForeignKey(Aula, null=False, blank=False, on_delete=models.CASCADE)
