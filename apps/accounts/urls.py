from django.contrib import admin
from django.urls import path, include
from .api.views import CreateUserAPIView

urlpatterns = [
    path('signup/', CreateUserAPIView.as_view(), name="sign-up"),
]
