from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import (
    PaymentListApiView,
    UserRetrieveApiView,
    UserUpdateApiView,
    UserDeleteApiView,
    UserListApiView,
    UserCreateApiView,
)

from django.urls import path

app_name = UsersConfig.name

urlpatterns = [
    path(
        "login/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="login",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token_refresh",
    ),
    path("<int:pk>/update/", UserUpdateApiView.as_view(), name="user_update"),
    path("retrieve/<int:pk>/", UserRetrieveApiView.as_view(), name="user_retrieve"),
    path("payment/", PaymentListApiView.as_view(), name="payment"),
    path("<int:pk>/delete/", UserDeleteApiView.as_view(), name="user_delete"),
    path("register/", UserCreateApiView.as_view(), name="user_register"),
    path("list/", UserListApiView.as_view(), name="user_list"),
]
