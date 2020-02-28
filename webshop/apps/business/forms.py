from django.forms import ModelForm
from .models import Bb, UserMessage
from django import forms


class BbForm(ModelForm):
    class Meta:
        model = Bb
        fields = ('title', 'content', 'price', 'image', 'rubric')


class UserMessageForm(ModelForm):
    class Meta:
        model = UserMessage
        fields = ('user_name', 'email', 'subject', 'message')
