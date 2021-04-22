from rest_framework.test import APITestCase, APIRequestFactory, APIClient
from rest_framework import status
from .models import Model


class KartaTestCase(APITestCase):
    client = APIClient()
    factory = APIRequestFactory
    car = {
        'carmake': 'honda',
        'model': 'cr-v'
    }

    def test_create_car(self):
        response = self.client.post('/cars/', self.car)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Model.objects.count(), 1)
        self.assertEqual(Model.objects.get().model, 'CR-V')

    def test_car_rate(self):
        response = self.client.post('/cars/', self.car)
        model_id = response.data['id']
        self.client.post('/rate/', {'model': model_id, 'rate': 1})
        self.client.post('/rate/', {'model': model_id, 'rate': 5})
        response = self.client.get('/popular/')
        self.assertEqual(response.data[0]['rate'], 2)

    def test_car_popular(self):
        response = self.client.post('/cars/', self.car)
        model_id = response.data['id']
        self.client.post('/rate/', {'model': model_id, 'rate': 1})
        self.client.post('/rate/', {'model': model_id, 'rate': 5})
        response = self.client.get('/popular/')
        self.assertEqual(response.data[0]['rate'], 2)

    def test_car_not_exists(self):
        car_not_exists = {
            'carmake': 'test_carmake',
            'model': 'test_model'
        }
        response = self.client.post('/cars/', car_not_exists)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
