# Generated by Django 4.1.2 on 2022-10-26 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="in_stock",
            field=models.BooleanField(default=True, verbose_name="В наличии"),
        ),
    ]
