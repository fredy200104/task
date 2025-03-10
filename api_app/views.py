from django.shortcuts import render

# Create your views here.
from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    biografia = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Editorial(models.Model):
    nombre = models.CharField(max_length=150)
    direccion = models.TextField()
    telefono = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    resumen = models.TextField()
    isbn = models.CharField(max_length=13, unique=True)
    anio_publicacion = models.PositiveIntegerField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='libros')
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE, related_name='libros')

    def __str__(self):
        return self.titulo

class Miembro(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    fecha_membresia = models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Prestamo(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='prestamos')
    miembro = models.ForeignKey(Miembro, on_delete=models.CASCADE, related_name='prestamos')
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.miembro} - {self.libro}"
