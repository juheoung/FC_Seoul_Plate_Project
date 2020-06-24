from rest_framework.routers import SimpleRouter

from review.views import ReviewViewSet

router = SimpleRouter(trailing_slash=False)
router.register('', ReviewViewSet, basename='reviews')
urlpatterns = router.urls
