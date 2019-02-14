from django import forms
from .models import Post

class BlogPostForm(forms.ModelForm):
	
    class Meta:
        model = Post
        fields = ('author', 'category', 'title', 'content', 'views', 'group', 'image',)