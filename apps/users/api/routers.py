from rest_framework.routers import DefaultRouter
from apps.users.api.views.user_viewset import UserViewSet,PlantsViewSet,UserRegisterViewSet,AdminRegisterViewSet



router = DefaultRouter()

router.register(r'user', UserViewSet, basename = 'user')
router.register(r'plants', PlantsViewSet, basename = 'plants')
router.register(r'registerClient', UserRegisterViewSet, basename = 'registerClient')
router.register(r'registerAdmin', AdminRegisterViewSet, basename = 'registerAdmin')


urlpatterns = router.urls 