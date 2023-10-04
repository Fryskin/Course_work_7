from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')

    phone_number = models.CharField(max_length=20, verbose_name='phone number', **NULLABLE)
    city = models.CharField(max_length=92, verbose_name='city', **NULLABLE)
    preview = models.ImageField(upload_to='images/users/', verbose_name='preview', **NULLABLE)
    telegram_id = models.CharField(max_length=100, verbose_name='telegram id', default='your telegram id')
    chat_id = models.CharField(max_length=1000, verbose_name='chat id',  **NULLABLE)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'User {self.email}'

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ('email',)
