from rest_framework import serializers
from .models import CarMake, Model, Rate
from .api import CarModelsApi


class ModelSerializer(serializers.ModelSerializer):
    carmake = serializers.CharField()
    rate = serializers.DecimalField(
        max_digits=5, decimal_places=2, read_only=True)
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Model
        fields = ('id', 'carmake', 'model', 'rate')

    def create(self, data):
        car_models = CarModelsApi(data)
        carmake, model = car_models.get_model_name()
        if carmake and model:
            # TODO: potrzebne przenieść do models save
            carmake, created = CarMake.objects.get_or_create(
                carmake=carmake
            )
            model, created = Model.objects.get_or_create(
                carmake=carmake, model=model
            )
            return model
        else:
            raise serializers.ValidationError(
                'No car models found for this request'
            )


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = '__all__'


class PopularSerializer(serializers.ModelSerializer):
    carmake = serializers.CharField(read_only=True)
    model = serializers.CharField(read_only=True)
    rate = serializers.IntegerField(read_only=True)
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Rate
        fields = ('id', 'carmake', 'model', 'rate')
