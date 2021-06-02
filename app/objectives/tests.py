from django.urls import reverse
# TESTOS DE CREACIO/REGISTRE
from objectives.models import Objective
from rest_framework import status
from rest_framework.test import APITestCase


class ObjectiveRegistrationAPIViewTestCase(APITestCase):
    def test_one_objective(self):
        """
        Test to verify that a post call with category
        """
        url = reverse('objective-list')
        data = {'objective': 'S'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Objective.objects.count(), 1)
        self.assertEqual(Objective.objects.get().objective, 'S')

    def test_error_objective(self):
        """
        Test to verify that a bad post call with category
        """
        url = reverse('objective-list')
        data = {'objective': 'Z'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Objective.objects.count(), 0)

    def test_two_objective(self):
        """
        Test to verify that a two post call with category
        """
        url = reverse('objective-list')
        data = {'objective': 'S'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        data = {'objective': 'P'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Objective.objects.count(), 2)
