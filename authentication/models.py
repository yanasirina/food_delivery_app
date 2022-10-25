from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class UserData(models.Model):
    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=15, blank=True, null=True, default=None)
    city = models.CharField(verbose_name='Город', max_length=30, blank=True, null=True, default=None)
    street = models.CharField(verbose_name='Улица', max_length=50, blank=True, null=True, default=None)
    house = models.IntegerField(verbose_name='Номер дома', blank=True, null=True, default=None)
    apartment = models.IntegerField(verbose_name='Номер квартиры', blank=True, null=True, default=None)

    class Meta:
        verbose_name = "Информация о пользователе"
        verbose_name_plural = "Информация о пользователях"

    def __str__(self):
        return str(self.user)
