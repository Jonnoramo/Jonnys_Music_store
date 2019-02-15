from django import forms
from .models import Thread, Post


class ThreadForm(forms.ModelForm):

    name = forms.CharField(label="Thread name")
    tag = forms.CharField(label="Tags")

    class Meta:
        model = Thread
        fields = ['name', 'tag']

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['comment']