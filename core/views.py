from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins, generics, viewsets
from rest_framework.permissions import IsAdminUser

from . import serializers
from . import models


class CategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

    @action(detail=True, methods=['get'])
    def items(self, request, pk):
        category = models.Category.objects.get(pk=pk)
        items = models.Item.objects.filter(category=category)
        items = [str(c) for c in items]
        return Response({'Товары': items})


class UpdateDeleteCategory(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser, )
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class CreateCategory(generics.CreateAPIView):
    permission_classes = (IsAdminUser, )
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
