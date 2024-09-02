import posixpath
from django.utils._os import safe_join
from django.views.static import serve as static_serve
from django.contrib.auth.models import User
from pathlib import Path
from rest_framework import viewsets, generics, views, response

from .models import Board, Post, Thread
from .serializers import BoardSerializer, PostSerializer, UserSerializer, ThreadInfoSerializer, PostsInThreadSerializer


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


class UserApi(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]


class PostsInThread(generics.RetrieveAPIView):
    serializer_class = PostsInThreadSerializer
    queryset = Thread.objects.all()


# class ThreadsInBoard(views.APIView):
#     pass


# class CreateNewThread(generics.CreateAPIView):
#     serializer_class = PostSerializer
#
#     def perform_create(self, serializer):
#         thread = self.kwargs['thread']
#         serializer.save(thread=thread)


# class CreateNewReply(generics.CreateAPIView):
#     serializer_class = PostSerializer
#
#     def perform_create(self, serializer):
#         thread = self.kwargs['thread']
#         serializer.save(thread=thread)
