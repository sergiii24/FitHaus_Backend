import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

# TESTOS DE CREACIO/REGISTRE
from categories.models import Category


class CategoryRegistrationAPIViewTestCase(APITestCase):
    def test_one_category(self):
        """
        Test to verify that a post call with category
        """
        url = reverse('category-list')
        data = {'category': 'S'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Category.objects.get().category, 'S')

    def test_error_category(self):
        """
        Test to verify that a bad post call with category
        """
        url = reverse('category-list')
        data = {'category': 'Z'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Category.objects.count(), 0)

    def test_two_category(self):
        """
        Test to verify that a two post call with category
        """
        url = reverse('category-list')
        data = {'category': 'S'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        data = {'category': 'Y'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 2)
