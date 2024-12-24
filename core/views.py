from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Workflow, Task
from .serializers import WorkflowSerializer, TaskSerializer


# Create your views here.
class WorkflowViewSet(viewsets.ModelViewSet):
    permission_classes= [IsAuthenticated]
    queryset = Workflow.objects.all()
    serializer_class = WorkflowSerializer


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
