from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Post Name'}))
    body = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Post Text'}))

    class Meta:
        model = Post
        fields = ['title', 'body', 'image']