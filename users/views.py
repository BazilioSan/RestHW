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

from .services import (
    create_stripe_product,
    create_stripe_price,
    create_stripe_session,
    prepare_data,
)
from datetime import date


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


class PaymentCreateApiView(CreateAPIView):

    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    def perform_create(self, serializer):
        # product = create_stripe_product()
        # price = create_stripe_price(product)
        # session_id, payment_link = create_stripe_session(price)
        # serializer.save(
        #     user=self.request.user,
        #     payment_date=date.today(),
        #     session_id=session_id,
        #     link_to_pay=payment_link,
        #     amount=price.get("unit_amount"),
        #     payment_method="безналичная оплата",
        # )

        type_bd = self.request.data.get(
            "type_bd"
        )  # получаем тип базы данных из запроса

        prod_id = self.request.data.get("prod_id")  # получаем id продукта из запроса

        price = self.request.data.get("price")  # получаем цену из запроса

        product_name, payment_obj = prepare_data(
            type_bd=type_bd, prod_id=prod_id
        )  # получаем название продукта и объект для привязки в оплате

        product = create_stripe_product(product_name)  # stripe создает продукт

        unit_price = create_stripe_price(product, price)  # stripe создает цену

        session_id, payment_link = create_stripe_session(
            unit_price
        )
        # stripe создаёт сессию и ссылку на оплату

        amount = unit_price["unit_amount"] / 100  # получаем цену в долларах
        # заполняем БД оплаты данными о платеже в зависимости от типа оплаченного продукта - курс либо урок

        if type_bd == "course":
            serializer.save(
                user=self.request.user,
                payment_date=date.today(),
                session_id=session_id,
                link_to_pay=payment_link,
                amount=amount,
                payment_method="безналичная оплата",
                course=payment_obj,
            )

        elif type_bd == "lesson":
            serializer.save(
                user=self.request.user,
                payment_date=date.today(),
                session_id=session_id,
                link_to_pay=payment_link,
                amount=amount,
                payment_method="безналичная оплата",
                lesson=payment_obj,
            )
