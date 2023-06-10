from rest_framework.routers import DefaultRouter
from apps.cactus.api.views.category_viewset import CategoryViewSet

router = DefaultRouter()
router.register(r'category',CategoryViewSet, basename = 'category')


urlpatterns = router.urls 