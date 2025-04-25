from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User
from projects.models import Project
from tasks.models import Task
from .models import Comment

class CommentTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='commenter', password='commentpass', role='developer')
        self.project = Project.objects.create(name='Test Project', owner=self.user)
        self.task = Task.objects.create(title='Test Task', project=self.project, assignee=self.user)
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_create_comment(self):
        data = {
            'content': 'This is a test comment',
            'author': self.user.id,
            'project': self.project.id,
            'task': self.task.id
        }
        response = self.client.post('/api/comments/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_comments(self):
        response = self.client.get('/api/comments/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
