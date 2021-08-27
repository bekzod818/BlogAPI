from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import PostViewSet, UserViewSet


router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('posts', PostViewSet, basename='posts')

urlpatterns = router.urls