from django import forms
from .models import Blog, Hashtag

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body', 'hashtags','image']

class HashtagForm(forms.ModelForm):
    class Meta:
        model = Hashtag
        fields = ['name']
