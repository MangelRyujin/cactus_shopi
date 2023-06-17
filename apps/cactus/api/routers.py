from rest_framework.routers import DefaultRouter
from apps.cactus.api.views.category_viewset import CategoryViewSet
from apps.cactus.api.views.plants_viewset import PlantsViewSet


router = DefaultRouter()
router.register(r'category',CategoryViewSet, basename = 'category')
router.register(r'plant',PlantsViewSet, basename = 'plant')




urlpatterns = router.urls 