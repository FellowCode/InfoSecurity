from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from utils.model_manager import MyUserManager


class User(AbstractBaseUser, PermissionsMixin):
    objects = MyUserManager()
    # Поля таблицы User
    email = models.EmailField(_('email address'), unique=True)

    last_name = models.CharField(max_length=128, verbose_name='Фамилия')
    first_name = models.CharField(max_length=128, verbose_name='Имя')
    surname = models.CharField(max_length=128, verbose_name='Отчество')

    is_staff = models.BooleanField(default=False, verbose_name='Персонал')
    is_active = models.BooleanField(default=True, verbose_name='Активный')
    date_joined = models.DateTimeField(default=timezone.now, verbose_name='Дата регистрации')

    dolzhnost = models.CharField(max_length=64, default='', verbose_name='Должность')

    gr_key = models.CharField(max_length=16, default=None, null=True, blank=True, verbose_name='Графический ключ')

    otdel = models.ForeignKey('Security.OtdelIR', on_delete=models.SET_NULL, related_name='users', null=True, default=None, verbose_name='Отдел')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_salt(self):
        return self.email

    class Meta:
        ordering = ['id']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
