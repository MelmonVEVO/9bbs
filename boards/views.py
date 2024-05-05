import posixpath
from django.utils._os import safe_join
from django.views.static import serve as static_serve
from django.contrib.auth.models import User
from pathlib import Path
from rest_framework import viewsets, permissions
from .models import Board, Post, Thread
from .serializers import BoardSerializer, PostSerializer, UserSerializer


def serve(request, path, document_root=None):
    path = posixpath.normpath(path).lstrip('/')
    fullpath = Path(safe_join(document_root, path))
    if fullpath.is_file():
        return static_serve(request, path, document_root)
    else:
        return static_serve(request, 'index.html', document_root)


class BoardApi(viewsets.ReadOnlyModelViewSet):
    queryset = Board.objects.all().order_by('board_index')
    serializer_class = BoardSerializer


class PostApi(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('post_last_modified')
    serializer_class = PostSerializer
    # permission_classes = [permissions.IsAuthenticated]


class ThreadApi(viewsets.ModelViewSet):
    queryset = Thread.objects.all().order_by('bump_timestamp')
    serializer_class = PostSerializer


class UserApi(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]
