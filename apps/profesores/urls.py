from profesores import views
from django.urls import path

urlpattern = [
   path('', teacher),
   path('<teacher_id>/', teacher),
]
