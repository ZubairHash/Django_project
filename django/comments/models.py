from django.db import models
from users.models import User
from projects.models import Project
from tasks.models import Task

class Comment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:50]
