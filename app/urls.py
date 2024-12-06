from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('post_detail/<int:pk>', post_detail, name='post_detail'),
    path('post_create/', post_create, name='post_create'),
    path('post_delete/<int:pk>', post_delete, name='post_delete'),
]
