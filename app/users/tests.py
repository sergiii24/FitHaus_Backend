from django.test import TestCase

# Create your tests here.

import json

from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase


# TESTOS DE CREACIO/REGISTRE
class UserRegistrationAPIViewTestCase(APITestCase):
    url = reverse("users:list")

    def test_invalid_password(self):
        """
        Test to verify that a post call with invalid passwords
        """
        user_data = {
            "username": "testuser",
            "firstname": "testfirstname",
            "lastname": "testlastname",
            "email": "test@testuser.com",
            "password": "123123",
            "gender": "K",  # DATA NO VALIDA (HAURIA DE SER M,F O X)
            "birthdate": "03-23-1990",  # DATA NO VALIDA (FORMAT CORRECTE: yyyy-mm-dd)
            "activitiesdone": "0",
            "achivements": "0",
            "points": "0",
            "level": "0",
            "objective": "0",
            "interestcategories": "0",
            "weight": "0",
            "height": "0",
            "imc": "0",
            "igc": "0"
        }
        response = self.client.post(self.url, user_data)
        self.assertEqual(400, response.status_code)

    def test_user_registration(self):
        """
        Test to verify that a post call with user valid data
        """
        user_data = {
            "username": "testuser",
            "firstname": "testfirstname",
            "lastname": "testlastname",
            "email": "test@testuser.com",
            "password": "123123",
            "gender": "M",
            "birthdate": "1990-03-23",
            "activitiesdone": "0",
            "achivements": "0",
            "points": "0",
            "level": "0",
            "objective": "0",
            "interestcategories": "0",
            "weight": "0",
            "height": "0",
            "imc": "0",
            "igc": "0"
        }
        response = self.client.post(self.url, user_data)
        self.assertEqual(201, response.status_code)
        self.assertTrue("token" in json.loads(response.content))

    def test_unique_username_validation(self):
        """
        Test to verify that a post call with already exists username
        """
        user_data_1 = {
            "username": "testuser",
            "firstname": "testfirstname",
            "lastname": "testlastname",
            "email": "test@testuser.com",
            "password": "123123",
            "gender": "M",
            "birthdate": "1990-03-23",
            "activitiesdone": "0",
            "achivements": "0",
            "points": "0",
            "level": "0",
            "objective": "0",
            "interestcategories": "0",
            "weight": "0",
            "height": "0",
            "imc": "0",
            "igc": "0"
        }
        response = self.client.post(self.url, user_data_1)
        self.assertEqual(201, response.status_code)

        user_data_2 = {
            "username": "testuser",
            "firstname": "testfirstname2",
            "lastname": "testlastname2",
            "email": "test2@testuser.com",
            "password": "123123",
            "gender": "M",
            "birthdate": "1990-03-23",
            "activitiesdone": "0",
            "achivements": "0",
            "points": "0",
            "level": "0",
            "objective": "0",
            "interestcategories": "0",
            "weight": "0",
            "height": "0",
            "imc": "0",
            "igc": "0"
        }
        response = self.client.post(self.url, user_data_2)
        self.assertEqual(400, response.status_code)


# TESTOS DE LOG IN
class UserLoginAPIViewTestCase(APITestCase):
    url = reverse("users:login")

    def setUp(self):
        self.email = "john@snow.com"
        self.password = "you_know_nothing"
        self.user = User.objects.create_user(self.email, self.password)

    def test_authentication_without_password(self):
        response = self.client.post(self.url, {"email": "snowman@mail.test"})
        self.assertEqual(400, response.status_code)

    def test_authentication_with_wrong_password(self):
        response = self.client.post(self.url, {"email": self.email, "password": "I_know"})
        self.assertEqual(400, response.status_code)

    def test_authentication_with_valid_data(self):
        response = self.client.post(self.url, {"email": self.email, "password": self.password})
        self.assertEqual(200, response.status_code)
        self.assertTrue("auth_token" in json.loads(response.content))





# ELS TESTOS SEGÜENTS NO SON NECESSARIS PER AQUEST SPRINT
# class UserTokenAPIViewTestCase(APITestCase):
#   def url(self, key):
#      return reverse("users:token", kwargs={"key": key})

# def setUp(self):
#    self.username = "john"
#   self.email = "john@snow.com"
#    self.password = "you_know_nothing"
#    self.user = User.objects.create_user(self.username, self.email, self.password)
#    self.token = Token.objects.create(user=self.user)
#    self.api_authentication()

#    self.user_2 = User.objects.create_user("mary", "mary@earth.com", "super_secret")
#    self.token_2 = Token.objects.create(user=self.user_2)

# def tearDown(self):
#     self.user.delete()
#     self.token.delete()
#     self.user_2.delete()
#     self.token_2.delete()

# def api_authentication(self):
#    self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

# def test_delete_by_key(self):
#     response = self.client.delete(self.url(self.token.key))
#     self.assertEqual(204, response.status_code)
#     self.assertFalse(Token.objects.filter(key=self.token.key).exists())

# def test_delete_current(self):
#    response = self.client.delete(self.url('current'))
#    self.assertEqual(204, response.status_code)
#    self.assertFalse(Token.objects.filter(key=self.token.key).exists())

# def test_delete_unauthorized(self):
#    response = self.client.delete(self.url(self.token_2.key))
#    self.assertEqual(404, response.status_code)
#    self.assertTrue(Token.objects.filter(key=self.token_2.key).exists())

# def test_get(self):
# Test that unauthorized access returns 404
#   response = self.client.get(self.url(self.token_2.key))
#   self.assertEqual(404, response.status_code)

#    for key in [self.token.key, 'current']:
#        response = self.client.get(self.url(key))
#        self.assertEqual(200, response.status_code)
#        self.assertEqual(self.token.key, response.data['auth_token'])
#        self.assertIn('created', response.data)
