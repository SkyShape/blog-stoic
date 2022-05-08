from django import forms
from django.forms import TextInput, Textarea, Select
from post.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'topic', 'description']
        widgets = {
            'title': TextInput(attrs={'placeholder': 'Please enter the title', 'class': 'form-control'}),
            'topic': Select(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'placeholder': 'Please enter the post content', 'class': 'form-control'}),
        }
