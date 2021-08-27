from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly


class PostViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, IsAuthorOrReadOnly)
    queryset =  Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(ModelViewSet):
    queryset =  get_user_model().objects.all()
    serializer_class = UserSerializer