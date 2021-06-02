from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

# TESTOS DE CREACIO/REGISTRE
from routines.models import Routine


class RoutineRegistrationAPIViewTestCase(APITestCase):
    def test_one_routine(self):
        """
        Test to verify that a post call with routine
        """
        url = reverse('category-list')
        data = {'category': 'S'}
        response = self.client.post(url, data, format='json')

        url = reverse('routine-list')
        act_data = {'name': 'E',
                    'description': 'Press',
                    'time': 'P',
                    'categories': None,
                    'exercises': None,
                    'classes': None}
        response = self.client.post(url, act_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Routine.objects.count(), 0)