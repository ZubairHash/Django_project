from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User
from .models import Project

class ProjectTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='owner', password='ownerpass', role='project_manager')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_create_project(self):
        data = {
            'name': 'Test Project',
            'description': 'A test project',
            'owner': self.user.id,
            'members': [self.user.id]
        }
        response = self.client.post('/api/projects/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_projects(self):
        response = self.client.get('/api/projects/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
