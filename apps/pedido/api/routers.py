from rest_framework.routers import DefaultRouter
from apps.pedido.api.views.car_viewset import CarViewSet


router = DefaultRouter()

router.register(r'car', CarViewSet, basename = 'car')


urlpatterns = router.urls 