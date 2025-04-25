from rest_framework import viewsets
from rest_framework.permissions import BasePermission, IsAuthenticated
from .models import Task
from .serializers import TaskSerializer

class IsTaskAssigneeOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return obj.assignee == request.user

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsTaskAssigneeOrReadOnly]
