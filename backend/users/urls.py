# users/urls.py
from django.urls import path

from .views import GoogleLoginAPIView, UserInfoAPIView

urlpatterns = [
    path('auth/google/', GoogleLoginAPIView.as_view(), name='google-login'),
    path('user-info', UserInfoAPIView.as_view(), name='user_info')
]
