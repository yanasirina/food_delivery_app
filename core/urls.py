from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [
    path('create_category/', views.CreateCategory.as_view(), name='create_category'),
    path('category/<int:pk>/', views.UpdateDeleteCategory.as_view(), name='retrieve_category'),
]

router = DefaultRouter()
router.register('categories', views.CategoryViewSet, basename='category')
urlpatterns += router.urls
