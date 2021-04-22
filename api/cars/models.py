from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class CarMake(models.Model):
    carmake = models.CharField(
        max_length=256, blank=False, unique=True)


class Model(models.Model):
    carmake = models.ForeignKey(
        CarMake, on_delete=models.CASCADE, related_name='models')
    model = models.CharField(max_length=256, blank=False)


class Rate(models.Model):
    model = models.ForeignKey(
        Model, on_delete=models.CASCADE, related_name='rates')
    rate = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(5)])
