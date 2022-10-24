from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class UserData(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=15)
    city = models.CharField(verbose_name='Город', max_length=30)
    street = models.CharField(verbose_name='Улица', max_length=50)
    house = models.IntegerField(verbose_name='Номер дома')
    apartment = models.IntegerField(verbose_name='Номер квартиры', blank=True, null=True)

    class Meta:
        verbose_name = "Информация о пользователе"
        verbose_name_plural = "Информация о пользователях"

    def __str__(self):
        return str(self.user)
