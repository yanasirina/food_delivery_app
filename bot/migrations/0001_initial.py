# Generated by Django 4.1.2 on 2022-10-24 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Courier",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "telegram_id",
                    models.IntegerField(
                        verbose_name="ID чата курьера с ботом в телеграме"
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Имя курьера")),
                (
                    "phone_number",
                    models.CharField(max_length=15, verbose_name="Номер телефона"),
                ),
                (
                    "is_able",
                    models.BooleanField(
                        default=False, verbose_name="Доступен к заказам"
                    ),
                ),
                (
                    "is_waiting_from",
                    models.DateTimeField(
                        blank=True,
                        default=None,
                        null=True,
                        verbose_name="Время ожидания нового заказа",
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="core.order",
                        verbose_name="Детали заказа",
                    ),
                ),
            ],
            options={
                "verbose_name": "Курьер",
                "verbose_name_plural": "Курьеры",
            },
        ),
    ]
