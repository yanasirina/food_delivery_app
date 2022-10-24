from django.db import models
from core.models import Order


class Courier(models.Model):
    telegram_id = models.IntegerField(verbose_name='ID чата курьера с ботом в телеграме')
    name = models.CharField(verbose_name='Имя курьера', max_length=255)
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=15)
    is_able = models.BooleanField(verbose_name='Доступен к заказам', default=False)
    is_waiting_from = models.DateTimeField(verbose_name='Время ожидания нового заказа',
                                           blank=True, null=True, default=None)
    order = models.ForeignKey(Order, verbose_name='Детали заказа',
                              blank=True, null=True, default=None, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "Курьер"
        verbose_name_plural = "Курьеры"

    def __str__(self):
        return f'{self.telegram_id}: {self.name}'
