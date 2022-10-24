from django.contrib import admin
from . import models


@admin.register(models.Courier)
class Courier(admin.ModelAdmin):
    list_display = ('telegram_id', 'name', 'phone_number')
    search_fields = ('telegram_id', 'name')
