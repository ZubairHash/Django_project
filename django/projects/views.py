from rest_framework import viewsets
from rest_framework.permissions import BasePermission, IsAuthenticated
from .models import Project
from .serializers import ProjectSerializer

class IsProjectOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return obj.owner == request.user

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsProjectOwnerOrReadOnly]
