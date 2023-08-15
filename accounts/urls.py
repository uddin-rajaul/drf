from django.urls import path
from accounts.views import RegisterAPIView, LogoutAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/login/', TokenObtainPairView.as_view(), name='login_view'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/',RegisterAPIView.as_view()),
    path('api/logout/', LogoutAPIView.as_view(), name='logout_view')
]
