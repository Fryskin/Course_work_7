
from rest_framework import status
from rest_framework.test import APITestCase

from useful_habits.models import UsefulHabit


class UsefulHabitsTestCase(APITestCase):
    def setUp(self) -> None:
        pass

    def test_create_useful_habit(self):
        """ The Testcase of creating the useful habit """
        data = {
            "location": "Home",
            "time": "13:54:58",
            "action": "Make a 10 push ups",
            "is_pleasant": False,
            "periodicity_in_hours": 1,
            "reward": "2000 deneg",
            "time_to_complete": "00:02:00",
            "is_public": True
        }

        response = self.client.post(
            '/useful_habit/create/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {'id': 1, 'location': 'Home', 'time': '13:54:58', 'action': 'Make a 10 push ups', 'is_pleasant': False,
             'periodicity_in_hours': 1, 'reward': '2000 deneg', 'time_to_complete': '00:02:00', 'is_public': True,
             'owner': None, 'associated_habit': None}
        )

        self.assertTrue(
            UsefulHabit.objects.all().exists()
        )

    def test_list_useful_habit(self):
        """ The Testcase of useful habit list's output """

        UsefulHabit.objects.create(
            location="Home",
            time="13:54:58",
            action="Make a 10 push ups",
            is_pleasant=False,
            periodicity_in_hours=1,
            reward="2000 deneg",
            time_to_complete="00:02:00",
            is_public=True
        )

        response = self.client.get(
            '/useful_habits/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'count': 1, 'next': None, 'previous': None, 'results': [
                {'id': 1, 'location': 'Home', 'time': '13:54:58', 'action': 'Make a 10 push ups', 'is_pleasant': False,
                 'periodicity_in_hours': 1, 'reward': '2000 deneg', 'time_to_complete':
                 '00:02:00', 'is_public': True, 'owner': None, 'associated_habit': None}]
             }

        )

    def test_update_useful_habit(self):
        """ The Testcase of update the useful habit """

        UsefulHabit.objects.create(
            location="Home",
            time="13:54:58",
            action="Make a 10 push ups",
            is_pleasant=False,
            periodicity_in_hours=1,
            reward="2000 deneg",
            time_to_complete="00:02:00",
            is_public=True
        )
        patch_data = {"location": "Street"}
        response = self.client.patch(
            '/useful_habit/update/1', patch_data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(response.json(),
                         {'id': 1, 'location': 'Street', 'time': '13:54:58', 'action': 'Make a 10 push ups',
                          'is_pleasant': False, 'periodicity_in_hours': 1, 'reward': '2000 deneg',
                          'time_to_complete': '00:02:00', 'is_public': True, 'owner': None, 'associated_habit': None}
                         )

    def test_delete_useful_habit(self):
        """ The Testcase of delete the useful habit """

        UsefulHabit.objects.create(
            location="Home",
            time="13:54:58",
            action="Make a 10 push ups",
            is_pleasant=False,
            periodicity_in_hours=1,
            reward="2000 deneg",
            time_to_complete="00:02:00",
            is_public=True
        )

        response = self.client.delete(
            '/useful_habit/delete/1'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
