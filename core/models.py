from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Category(models.Model):
    name = models.CharField(verbose_name='Категория', max_length=100)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Список Категорий"

    def __str__(self):
        return self.name


class Item(models.Model):
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.PROTECT)
    name = models.CharField(verbose_name='Название товара', max_length=255)
    description = models.TextField(verbose_name='Описание товара', blank=True, null=True)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Список Товаров"

    def __str__(self):
        return self.name


class Order(models.Model):
    items = models.ManyToManyField(Item, verbose_name='Товары')
    user = models.ForeignKey(User, verbose_name='Покупатель', on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name="Изменено", auto_now=True)
    is_ordered = models.BooleanField(verbose_name='Заказ оформлен', default=False)
    is_delivered = models.BooleanField(verbose_name='Заказ доставлен', default=False)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f'{str(self.user)}: {self.date}'
