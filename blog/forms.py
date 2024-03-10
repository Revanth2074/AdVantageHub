from django.forms import ModelForm
from .models import Post, Comment
from django import forms
from django.core.exceptions import ValidationError
import datetime
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm:
    def __init__(self, data=None, **kwargs):
        if data is not None:
            self.username = data.get('username')
            self.email = data.get('email')
            self.password = data.get('password')
        else:
            self.username = None
            self.email = None
            self.password = None

class PostForm:
    def __init__(self, data):
        self.title = data['title']
        self.content = data['content']
        self.user_id = data['user_id']

class CommentForm:
    def __init__(self, data):
        self.content = data['content']
        self.user_id = data['user_id']
        self.post_id = data['post_id']