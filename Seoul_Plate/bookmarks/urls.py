from rest_framework.routers import SimpleRouter
from .views import BookMarkViewSet

router = SimpleRouter()
router.register('', BookMarkViewSet)
urlpatterns = router.urls
