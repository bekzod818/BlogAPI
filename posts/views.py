from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .serializer import PostSerializer
from .permissions import IsAuthorOrReadOnly


class PostList(ListCreateAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, IsAuthorOrReadOnly)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
