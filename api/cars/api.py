import json
import requests
from rest_framework import serializers


class CarModelsApi:
    def __init__(self, data):
        self.carmake = data['carmake'].upper()
        self.model = data['model'].upper()

    def connection(self):
        url = f'https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{self.carmake}?format=json'
        response = requests.get(url)
        return response.text

    def get_model_name(self):
        try:
            url_data = json.loads(self.connection())
            results = url_data.get('Results', [])
            for res in results:
                if res.get('Model_Name').upper() == self.model:
                    return self.carmake, self.model
            return None, None
        except Exception as e:
            raise serializers.ValidationError(str(e))
