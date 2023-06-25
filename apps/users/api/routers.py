from rest_framework.routers import DefaultRouter
from apps.users.api.views.user_viewset import UserViewSet,PlantsViewSet,UserRegisterViewSet



router = DefaultRouter()

router.register(r'user', UserViewSet, basename = 'user')
router.register(r'plants', PlantsViewSet, basename = 'plants')
router.register(r'register', UserRegisterViewSet, basename = 'register')


urlpatterns = router.urls 