from django.contrib.auth.models import Group, User
from rest_framework import serializers
from boards.models import Board, Post, Thread


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'url']


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['board_index', 'board_name']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'post_no',
            'poster',
            'thread',
            'reply_to',
            'post_title',
            'post_body',
            'post_date',
            'post_last_modified'
        ]
        read_only_fields = ['post_date']


class ThreadInfoSerializer(serializers.ModelSerializer):
    first_post = PostSerializer(many=False, read_only=True)

    class Meta:
        model = Thread
        fields = [
            'id',
            'thread_title',
            'board',
            'archived',
            'sticky',
            'first_post'
        ]


class PostsInThreadSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Thread
        fields = [
            'id',
            'thread_title',
            'board',
            'archived',
            'sticky',
            'posts'
        ]
