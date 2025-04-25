from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User

class UserTests(APITestCase):
    def setUp(self):
        self.admin_user = User.objects.create_user(username='admin', password='adminpass', role='admin')
        self.token = Token.objects.create(user=self.admin_user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_create_user(self):
        data = {
            'username': 'testuser',
            'password': 'testpass',
            'role': 'developer'
        }
        response = self.client.post('/api/users/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_users(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
