from django.contrib import admin
from . import models


@admin.register(models.UserData)
class UserData(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'city')
    autocomplete_fields = ('user', )
