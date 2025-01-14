from rest_framework.generics import UpdateAPIView, ListAPIView, RetrieveAPIView
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from users.models import User, Payment
from users.serializers import UserSerializer, PaymentSerializer


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
