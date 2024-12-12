from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Введите ваш юзернейм"})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Придумайте пароль"})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Повторите пароль"})
    )

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Введите ваш юзернейм"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Введите пароль"})
    )

    class Meta:
        model = User
        fields = ["username", "password"]
