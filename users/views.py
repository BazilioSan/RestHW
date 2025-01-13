from rest_framework.decorators import permission_classes
from rest_framework.generics import (
    UpdateAPIView,
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
)
from rest_framework import filters
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend

from users.models import User, Payment
from users.serializers import UserSerializer, PaymentSerializer


class UserCreateApiView(CreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = User.objects.all()
        user.set_password(user.password)
        user.save()


class UserDeleteApiView(DestroyAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserListApiView(ListAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateApiView(UpdateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveApiView(RetrieveAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class PaymentListApiView(ListAPIView):

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ("course", "lesson", "payment_method")
    ordering_fields = "payment_date"
