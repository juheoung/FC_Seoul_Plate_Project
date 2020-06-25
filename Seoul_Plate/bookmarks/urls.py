from rest_framework.routers import SimpleRouter

from bookmarks.views import BookMarkViewSet

router = SimpleRouter(trailing_slash=False)
router.register('', BookMarkViewSet)
urlpatterns = router.urls
