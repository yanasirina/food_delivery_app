from rest_framework import serializers

from . import models


class CourierSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Courier
        fields = ('telegram_id', 'name', 'phone_number')
