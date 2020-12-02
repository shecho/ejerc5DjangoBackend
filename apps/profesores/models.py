from django.db import models


class Teacher(models.Model):
   name = models.CharField(max_length=120, blank=True, null=False)
   last_name = models.CharField(max_length=120, blank=True, null=False)
   phone = models.CharField(max_length=20, blank=True, null=False)
   email = models.EmailField(max_length=120, blank=True, null=False)
   active = models.BooleanField(default=False)

   class Meta:
      ordering = ['name']
      verbose_name = 'Teacher'
      verbose_name_plural = 'Teachers'

   def __str__(self):
      return self.name, + ' ' + self.last_name
