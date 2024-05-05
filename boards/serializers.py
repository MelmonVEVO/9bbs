from django.contrib.auth.models import Group, User
from rest_framework import serializers
from boards.models import Board, Post, Thread


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'url']


class BoardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Board
        fields = ['board_name', 'board_index']


class ThreadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Thread
        field = [
            'id',
            'thread_title',
            'bump_timestamp',
            'board',
            'archived',
            'sticky'
        ]


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = [
            'poster',
            'thread',
            'post_no',
            'reply_to',
            'post_title',
            'post_body',
            'post_date',
            'post_last_modified'
        ]


class NewPostDeserializer(serializers.ModelSerializer):
    pass