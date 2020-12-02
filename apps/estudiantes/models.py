from django.db import models

class Student(models.Model):
   nombre = models.CharField(max_length=120, blank=True, null=False)
   apellidos = models.CharField(max_length=120, blank=True, null=False)
   telefono = models.CharField(max_length=20, blank=True, null=False)
   email = models.EmailField(max_length=120, blank=True, null=False)
   activo = models.BooleanField(default=False)

class Meta:
   ordering = ['nombre']
   verbose_name = 'Student'
   verbose_name_plural = 'Students'

   def __init__(self):
      self.nombre = None

   def __str__(self):
      return self.nombre
