#from django.shortcuts import render
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
# Create your views here.

class Tasks(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class ViewTask(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'id'