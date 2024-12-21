from django.db import models

class User(AbstractUser):
    """User model"""

    username = None
    email = models.EmailField(unique=True, verbose_name="Email")
    first_name = models.CharField(max_length=50, verbose_name="First name", blank=True, null=True, help_text="Enter username")
    last_name = models.CharField(max_length=50, verbose_name="Last name", blank=True, null=True, help_text="Enter surname")
    phone_number = models.CharField(max_length=15, verbose_name="Phone number", blank=True, null=True, help_text="Enter phone number")
    avatar = models.ImageField(upload_to="users/avatars", verbose_name="Avatar", blank=True, null=True, help_text="Upload avatar")
    city = models.CharField(max_length=50, verbose_name="City", blank=True, null=True, help_text="Enter city")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
