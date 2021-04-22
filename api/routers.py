from rest_framework.routers import DefaultRouter, SimpleRouter
from .cars.views import ModelViewSet, RateViewSet, PopularViewSet
from django.conf import settings
if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register(r'cars', ModelViewSet)
router.register(r'rate', RateViewSet)
router.register(r'popular', PopularViewSet)
urlpatterns = router.urls
