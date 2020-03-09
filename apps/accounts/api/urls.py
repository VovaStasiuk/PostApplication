from django.urls import path

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from .views import CreateUserAPIView

urlpatterns = [
    path('signup/', CreateUserAPIView.as_view(), name='account-signup'),
    path('login/', obtain_jwt_token, name='account-login'),
    path('refresh/', refresh_jwt_token),
]