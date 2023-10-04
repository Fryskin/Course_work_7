from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from users.apps import UsersConfig
from users.views import UserListCreateView, UserDetailView

app_name = UsersConfig.name

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path("all_profiles", UserListCreateView.as_view(), name="all_profiles"),
    path("profile/<int:pk>", UserDetailView.as_view(), name="profile")
]
