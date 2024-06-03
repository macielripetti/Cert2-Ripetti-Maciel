from django.db import models
# Create your models here.
class Tema(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    

class Proyecto(models.Model):
    nombrep = models.CharField(max_length=200, verbose_name="NombreP")
    estudiante = models.CharField(max_length=200, verbose_name="Estudiante")
    tema = models.CharField(max_length=200, verbose_name="Tema")
    profesor = models.CharField(max_length=200, blank=True, null=True, verbose_name="Profesor")
    email = models.EmailField(max_length=50, verbose_name="email")
    descripcion = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.nombrep
