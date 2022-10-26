from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [

]

router = DefaultRouter()
router.register('couriers', views.CourierViewSet, basename='courier')
urlpatterns += router.urls
