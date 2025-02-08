from django.urls import path
from .views import register_user, login_user,protected_view
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('protected_view/', protected_view, name='protected_view'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
