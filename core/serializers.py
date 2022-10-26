from rest_framework import serializers

from . import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Item
        fields = '__all__'


class ItemGetSerializer(ItemSerializer):
    category = CategorySerializer()


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        exclude = ('user', 'is_ordered', 'is_delivered')


class OrderAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = '__all__'

