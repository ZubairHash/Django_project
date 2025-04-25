from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User
from projects.models import Project
from .models import Task

class TaskTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='developer', password='devpass', role='developer')
        self.project = Project.objects.create(name='Test Project', owner=self.user)
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_create_task(self):
        data = {
            'title': 'Test Task',
            'description': 'A test task',
            'project': self.project.id
        }
        response = self.client.post('/api/tasks/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_tasks(self):
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
