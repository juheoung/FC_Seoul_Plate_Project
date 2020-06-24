from rest_framework.routers import SimpleRouter

from blogs.views import BlogViewSet

router = SimpleRouter()

router.register('blogs', BlogViewSet)
urlpatterns = router.urls
