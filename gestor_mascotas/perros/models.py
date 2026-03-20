from django.db import models

# Create your models here.
class Raza(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    vida_min = models.IntegerField()
    vida_max = models.IntegerField()
    hipoalergenico = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre