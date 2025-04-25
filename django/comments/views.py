from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, BasePermission
from .models import Comment
from .serializers import CommentSerializer

class IsCommentAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return obj.author == request.user

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsCommentAuthorOrReadOnly]
