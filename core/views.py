from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins, generics, viewsets
from rest_framework.permissions import IsAdminUser

from . import serializers
from . import models


class CategoryViewSet(ReadOnlyModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

    @action(detail=True, methods=['get'])
    def items(self, request, pk):
        category = models.Category.objects.get(pk=pk)
        items = models.Item.objects.filter(category=category)
        items = [str(c) for c in items]
        return Response({'Товары': items})


class AdminCategoryViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin, viewsets.GenericViewSet):
    permission_classes = (IsAdminUser, )
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class ItemViewSet(ReadOnlyModelViewSet):
    queryset = models.Item.objects.all()
    serializer_class = serializers.ItemGetSerializer


class AdminItemViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin, viewsets.GenericViewSet):
    permission_classes = (IsAdminUser,)
    queryset = models.Item.objects.all()
    serializer_class = serializers.ItemSerializer

