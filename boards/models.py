from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Board(models.Model):
    board_index = models.CharField(max_length=4, primary_key=True)
    board_name = models.CharField(max_length=70)

    def __str__(self):
        return self.board_name


class Thread(models.Model):
    thread_title = models.CharField(max_length=100, blank=True)
    bump_timestamp = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    archived = models.BooleanField(default=False)
    sticky = models.BooleanField(default=False)

    def __str__(self):
        return self.thread_title


class Post(models.Model):
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    post_no = models.IntegerField(default=0)
    reply_to = models.ForeignKey("self", blank=True, null=True, on_delete=models.CASCADE)
    post_body = models.CharField(max_length=800)
    post_date = models.DateTimeField(auto_now_add=True)
    post_last_modified = models.DateTimeField(auto_now=True, editable=True)

    class Meta:
        ordering = ['post_no']

    def __str__(self):
        return f'Thread {self.thread} # {self.post_no}'
