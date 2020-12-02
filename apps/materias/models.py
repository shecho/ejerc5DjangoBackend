from django.core.validators import MinLengthValidator
from django.db import models

from ..estudiantes.models import Student
from ..profesores.models import Teacher


class Materia(models.Model):
   code = models.CharField(max_length=20)
   name = models.CharField(max_length=150, validators=[MinLengthValidator(4)])
   credit = models.IntegerField(blank=True, null=False, validators=[MinLengthValidator(2)])
   active = models.BooleanField(default=False)
   description = models.CharField(max_length=200, blank=True, null=False)

   area = models.ForeignKey(Student, on_delete=models.PROTECT)
   managers = models.ManyToManyField(Teacher, related_name='Estudiante')

   class Meta:
      ordering = ['code']
      verbose_name = 'Materia'
      verbose_name_plural = 'Materias'

   def __str__(self):
      return self.name
