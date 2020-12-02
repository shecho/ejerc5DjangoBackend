from django.shortcuts import render

from rest_framework import status
from rest_restframework.decorators import api_view
from rest_framework.response import Response

from .serializers import TeacherSerializer
from .models import Teacher

@api_view(['GET', 'POST'])
def teacher_list(request):

   if method == 'GET':
      teachers = Teacher.objects.all()
      serializer = TeacherSerializer(teachers, many=True)
      return Response(serializer.data)

   elif request.method == 'POST':
      serializer = TeacherSerializer(data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, HTTP_201_CREATED)
      return Response(serializer.errors, status.HTTP_BAD_REQUEST)
