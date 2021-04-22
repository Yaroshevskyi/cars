from rest_framework import viewsets
from .models import Model, Rate
from .serializers import ModelSerializer, RateSerializer, PopularSerializer
from django.db.models import Count, F, Avg
from django.db.models.functions import Coalesce


class ModelViewSet(viewsets.ModelViewSet):
    """
    Rest API list of all cars already present in
    application database with their current average rate.
    """
    serializer_class = ModelSerializer
    queryset = Model.objects.values(
        'id', 'carmake__carmake', 'model'
        ).annotate(
            carmake=F('carmake__carmake'),
            rate=Avg(Coalesce('rates__rate', 0))
        ).order_by('-rate')
    http_method_names = ['get', 'post']


class RateViewSet(viewsets.ModelViewSet):
    """
    Rest API add a rate for a car from 1 to 5.
    """
    serializer_class = RateSerializer
    queryset = Rate.objects.all()
    http_method_names = ['post']


class PopularViewSet(viewsets.ModelViewSet):
    """
    Rest API top cars already present in the database
    ranking based on number of rates
    """
    serializer_class = PopularSerializer
    queryset = Rate.objects.values(
        'model__carmake__carmake', 'model__model').annotate(
            carmake=F('model__carmake__carmake'),
            model=F('model__model'),
            rate=Count('id')
        ).order_by('-rate')
    http_method_names = ['get']
