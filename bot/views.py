from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from . import models
from . import serializers


class CourierViewSet(ModelViewSet):
    permission_classes = (IsAdminUser, )
    queryset = models.Courier.objects.all()
    serializer_class = serializers.CourierSerializer
