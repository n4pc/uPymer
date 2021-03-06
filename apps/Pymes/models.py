from django.db import models

# Create your models here.

class Cat(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    img = models.ImageField(upload_to='categorias')

    def __str__(self):
        return self.nombre

class Pyme(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255)
    rut_empresa = models.CharField(max_length=10)
    direccion = models.CharField(max_length=50)
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='Pymes')

    def __str__(self):
        return self.nombre



class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    precio = models.IntegerField()
    pyme = models.ForeignKey(Pyme, blank=True, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='productos')

    def __str__(self):
        return self.nombre

