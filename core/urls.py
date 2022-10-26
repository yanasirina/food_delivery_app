from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [

]

router = DefaultRouter()
router.register('admin_categories', views.AdminCategoryViewSet, basename='admin_category')
router.register('categories', views.CategoryViewSet, basename='category')
router.register('items', views.ItemViewSet, basename='item')
router.register('admin_items', views.AdminItemViewSet, basename='admin_item')
urlpatterns += router.urls
