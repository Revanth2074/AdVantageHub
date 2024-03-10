from .models import Post, Comment
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm


class UserAdmin:
    def __init__(self, user):
        self.username = user.username
        self.email = user.email
        self.password = user.password


class PostAdmin:
    def __init__(self, post):
        self.title = post.title
        self.content = post.content
        self.user_id = post.user_id
        self.created_at = post.created_at


class CommentAdmin:
    def __init__(self, comment):
        self.content = comment.content
        self.user_id = comment.user_id
        self.post_id = comment.post_id
        self.created_at = comment.created_at
