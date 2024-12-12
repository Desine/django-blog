from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login, logout

def register(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect("users:login")

    return render(request, "register.html", {"form": form})

def log_in(request):
    form = LoginForm(data=request.POST or None)

    if form.is_valid() and request.method == "POST":
        user = form.get_user()
        login(request, user)
        return redirect("app:home")

    return render(request, "login.html", {"form": form})

def log_out(request):
    if request.method == "POST":
        logout(request)
        return redirect("users:login")

    return render(request, "logout.html")