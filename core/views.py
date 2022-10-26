from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated

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

    def get_queryset(self):
        return models.Item.objects.filter(in_stock=True)


class AdminItemViewSet(ModelViewSet):
    permission_classes = (IsAdminUser, )
    queryset = models.Item.objects.all()
    serializer_class = serializers.ItemSerializer

    @action(detail=True, methods=['patch'])
    def set_in_stock(self, request, pk):
        item = self.get_object()
        if not item.in_stock:
            item.in_stock = True
            item.save(update_fields=['in_stock'])
        serializer = serializers.ItemSerializer(instance=item)
        return Response(serializer.data)

    @action(detail=True, methods=['patch'])
    def unset_in_stock(self, request, pk):
        item = self.get_object()
        if item.in_stock:
            item.in_stock = False
            item.save(update_fields=['in_stock'])
        serializer = serializers.ItemSerializer(instance=item)
        return Response(serializer.data)


class AdminOrderViewSet(ReadOnlyModelViewSet):
    permission_classes = (IsAdminUser, )
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderAdminSerializer


class OrderViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer

    def get_queryset(self):
        return models.Order.objects.filter(user=self.request.user, is_ordered=False)

    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        super().perform_create(serializer)

    """Шаблон для дальнейшего добавления в бот"""
    # @action(detail=True, methods=['patch'])
    # def to_order(self, request, pk):
    #     order = self.get_object()
    #     order.is_ordered = True
    #     order.save(update_fields=['is_ordered'])
    #     serializer = serializers.ItemSerializer(instance=order)
    #     return Response(serializer.data)


class FinishedOrderViewSet(ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer

    def get_queryset(self):
        return models.Order.objects.filter(user=self.request.user, is_ordered=True)

    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        super().perform_create(serializer)
