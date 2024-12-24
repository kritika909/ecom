from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenBlacklistView,
    TokenRefreshView,
)
from .views import signup

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('logout/', TokenBlacklistView.as_view(), name='token_blacklist'),
]