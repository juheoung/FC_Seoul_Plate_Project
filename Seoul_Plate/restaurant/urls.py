from rest_framework.routers import SimpleRouter
from restaurant.views import RestViewSet

router = SimpleRouter(trailing_slash=False)
router.register('', RestViewSet, basename='restaurant')
urlpatterns = router.urls
