from django.test import TestCase
from django.contrib.auth.models import User
from django.test.client import Client
import unittest

# create user test
class UserSignupTest(TestCase):
    def setup(self):
        return

    def test_signup(self):
        response = self.client.post('/auth/signup', {'username': 'test name', 'password1': 'aK7h%]1Nm84', 'email': 'test@gmail.com'})
        self.assertEquals(response.status_code, 302)

# change pw test
class UserPwChangeTest(TestCase):
    def setup(self):
        self.client = Client()
        

    def test_delete(self):
        self.user = User.objects.create_user(username='test2', password='1234')
        login = self.client.login(username='test2', password='1234')
        print(login)
        response = self.client.post('/auth/changePassword', {'newpw': '12345678', 'confirm': '123456', 'oldpw': '1234'})
        self.assertEquals(response.status_code, 200)
        response = self.client.post('/auth/changePassword', {'newpw': '12345678', 'confirm': '12345678', 'oldpw': '1234'})
        self.assertEquals(response.status_code, 200)

# delete user test
class UserDeleteTest(TestCase):
    def setup(self):
        self.client = Client()
        self.user = User.objects.create_user('test', 'test@test.com', 'testpw')

    def test_delete(self):
        self.client.login(username='test', password='testpw')
        response = self.client.post('/auth/deleteAccount')
        self.assertEquals(response.status_code, 302)