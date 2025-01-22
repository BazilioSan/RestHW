from django.contrib.auth.models import AbstractUser
from django.db import models

from lms.models import Lesson, Course


class User(AbstractUser):
    """User model"""

    username = None
    email = models.EmailField(unique=True, verbose_name="Email")
    first_name = models.CharField(
        max_length=50,
        verbose_name="First name",
        blank=True,
        null=True,
        help_text="Enter username",
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name="Last name",
        blank=True,
        null=True,
        help_text="Enter surname",
    )
    phone_number = models.CharField(
        max_length=15,
        verbose_name="Phone number",
        blank=True,
        null=True,
        help_text="Enter phone number",
    )
    avatar = models.ImageField(
        upload_to="users/avatars",
        verbose_name="Avatar",
        blank=True,
        null=True,
        help_text="Upload avatar",
    )
    city = models.CharField(
        max_length=50,
        verbose_name="City",
        blank=True,
        null=True,
        help_text="Enter city",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email


class Payment(models.Model):
    """Payment model"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        null=True,
        blank=True,
    )
    payment_date = models.DateTimeField(
        verbose_name="Дата оплаты",
        help_text="Дата оплаты",
        null=True,
        blank=True,
    )
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, verbose_name="Оплаченный Курс"
    )
    lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, verbose_name="Оплаченный Урок"
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Сумма оплаты",
        null=True,
        blank=True,
    )
    session_id = models.CharField(
        max_length=255, verbose_name="ID сессии", blank=True, null=True
    )
    link_to_pay = models.URLField(
        max_length=400, verbose_name="Ссылка на оплату", blank=True, null=True
    )

    CASH = "Наличные"
    CARD = "Карта"
    PAYMENT_CHOICE = [(CASH, "Наличные"), (CARD, "Безналичная")]
    payment_method = models.CharField(
        max_length=20,
        verbose_name="Метод оплаты",
        help_text="Способ оплаты",
        choices=PAYMENT_CHOICE,
        default=CARD,
    )

    class Meta:
        verbose_name = "Оплата"
        verbose_name_plural = "Оплаты"

    def __str__(self):
        return f"{self.user.email} - {self.payment_date} - {self.payment_method}"
