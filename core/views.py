import requests
from decouple import config

from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from . import serializers
from . import models
from authentication.models import UserData
from bot.models import Courier


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

    @action(detail=True, methods=['patch'])
    def to_order(self, request, pk):
        order = self.get_object()
        user = order.user
        user_data = UserData.objects.filter(user=user).first()
        try:
            if user_data.city and user_data.street and user_data.house and user_data.phone_number:
                address = f'{user_data.city}, {user_data.street}, {user_data.house}, {user_data.apartment}'
                phone = str(user_data.phone_number)
                text = f'Address:\n{address}\nPhone:\n{phone}'

                courier = Courier.objects.filter(is_able=True).order_by('is_waiting_from').first()
                telegram_id = courier.telegram_id
                txt = f"https://api.telegram.org/bot" \
                      f"{config('TOKEN')}/sendMessage?" \
                      f"chat_id={telegram_id}&" \
                      f"text={text}"
                requests.get(txt)

                order.is_ordered = True
                order.save(update_fields=['is_ordered'])

                courier.is_able = False
                courier.is_waiting_from = None
                courier.order = order
                courier.save(update_fields=['is_able', 'is_waiting_from', 'order'])
            else:
                return Response({'error': 'Вы указали неполную информацию о себе'})
            return Response({'status': 'Мы приступили к сборке вашего заказа'})
        except Exception:
            return Response({'error': 'Нет свободных курьеров'})


class FinishedOrderViewSet(ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer

    def get_queryset(self):
        return models.Order.objects.filter(user=self.request.user, is_ordered=True)

    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        super().perform_create(serializer)
