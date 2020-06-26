from rest_framework.routers import SimpleRouter
from restaurant.views import RestViewSet, RestDetailViewSet

router = SimpleRouter(trailing_slash=False)
router.register('', RestViewSet, basename='restaurant')
router.register('', RestDetailViewSet, basename='restaurant')
urlpatterns = router.urls
