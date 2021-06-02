from django.urls import reverse
# TESTOS DE CREACIO/REGISTRE
from exercises.models import Exercise
from rest_framework import status
from rest_framework.test import APITestCase


class ExerciseRegistrationAPIViewTestCase(APITestCase):
    def test_one_bad_file_exercise(self):
        """
        Test to verify that a post call with category
        """
        url = reverse('classes-list')
        act_data = {'activity': 'Bad_test',
                    'muscleimage': None,
                    'videotutorial': None,
                    'videoexercise': None,
                    'workarea': 'Bi'}
        response = self.client.post(url, act_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
        self.assertEqual(Exercise.objects.count(), 0)
