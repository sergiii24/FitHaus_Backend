
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

# TESTOS DE CREACIO/REGISTRE
from classes.models import Classes


class ClassesRegistrationAPIViewTestCase(APITestCase):
    def test_one_bad_file_classes(self):
        """
        Test to verify that a post call with category
        """
        url = reverse('classes-list')
        act_data = {'activity': 'Bad_test',
                    'videoclass': None,
                    'trainer': 'Ex',
                    'workarea': 'T'}
        response = self.client.post(url, act_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
        self.assertEqual(Classes.objects.count(), 0)
