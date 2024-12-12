from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Название поста"}),
    )
    body = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Текст поста"})
    )

    class Meta:
        model = Post
        fields = ["title", "body", "image"]
