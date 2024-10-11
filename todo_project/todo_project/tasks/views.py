#from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import  api_view
from rest_framework.response import Response
from datetime import date

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

@api_view(['GET'])
def FilterTask(request):
    query = request.GET.get('query')
    status = request.GET.get('status')

    if not query:
        query = ''
    
    filtertask = Task.objects.filter(title__icontains=query)

    if status == 'incoming':
        filtertask = filtertask.filter(due_date__gt=date.today())
    elif status == 'today':
        filtertask = filtertask.filter(due_date=date.today())
    elif status == 'overdue':
        filtertask = filtertask.filter(due_date__lt=date.today())
    
    serializer = TaskSerializer(filtertask, many=True)
    return Response(serializer.data)