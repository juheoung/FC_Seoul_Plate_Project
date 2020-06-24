from rest_framework.routers import SimpleRouter

from user.views import UserViewSet

router = SimpleRouter(trailing_slash=False)
router.register('', UserViewSet)
urlpatterns = router.urls
