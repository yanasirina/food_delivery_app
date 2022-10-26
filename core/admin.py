from django.contrib import admin
from . import models


@admin.register(models.Category)
class Category(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )


@admin.register(models.Item)
class Item(admin.ModelAdmin):
    list_display = ('name', 'in_stock')
    search_fields = ('name', )
    list_filter = ('in_stock', )
    list_editable = ('in_stock',)
    autocomplete_fields = ('category', )


@admin.register(models.Order)
class Order(admin.ModelAdmin):
    list_display = ('user', 'date', 'is_ordered', 'is_delivered')
    autocomplete_fields = ('user', 'items')
    list_editable = ('is_ordered', 'is_delivered')
    list_filter = ('is_ordered', 'is_delivered', 'date')
