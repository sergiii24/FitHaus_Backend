
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

# TESTOS DE CREACIO/REGISTRE
from activities.models import Activity


class ActivityRegistrationAPIViewTestCase(APITestCase):
    def test_one_bad_file_activity(self):
        """
        Test to verify that a post call with category
        """
        url = reverse('category-list')
        data = {'category': 'S'}
        response = self.client.post(url, data, format='json')

        url = reverse('activity-list')
        act_data = {'type': 'E',
                    'name': 'Press',
                    'description': 'Ex',
                    'age': 'T',
                    'difficulty': 'E',
                    'length': '2',
                    'categories': 'S',
                    'pre': None}
        response = self.client.post(url, act_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
        self.assertEqual(Activity.objects.count(), 0)
