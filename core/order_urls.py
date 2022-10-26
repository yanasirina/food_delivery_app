from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [

]

router = DefaultRouter()
router.register('all_orders', views.AdminOrderViewSet, basename='admin_order')
router.register('user_orders', views.OrderViewSet, basename='user_order')
router.register('user_finished_orders', views.FinishedOrderViewSet, basename='user_finished_order')
urlpatterns += router.urls
