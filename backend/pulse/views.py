from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
  queryset = Task.objects.all()
  serializer_class = TaskSerializer
  
  @action(detail=True, methods=['post'])
  def complete(self, request, pk=None):
    task = self.get_object()
    task.is_completed = True
    task.save()
    return Response({'status': 'task marked as complete'}, status=status.HTTP_200_OK)
  
  @action(detail=True, methods=['post'])
  def incomplete(self, request, pk=None):
    task = self.get_object()
    task.is_completed = False
    task.save()
    return Response({'status': 'task marked as incomplete'}, status=status.HTTP_200_OK)