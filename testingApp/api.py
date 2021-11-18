from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import PrivateApiView, PublicApiView

urlpatterns = [
    
    path('private/', PrivateApiView.as_view(), name='private'),
    path('public/', PublicApiView.as_view(), name='public'),
    
]