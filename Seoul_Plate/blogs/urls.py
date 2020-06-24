from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import SimpleRouter

from blogs.views import BlogViewSet

router = SimpleRouter()

router.register('', BlogViewSet)
urlpatterns = router.urls
