from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.RegisterUser.as_view(), name='user_register'),
    path('login/', views.LoginUser.as_view(), name='user_login'),
    path('user_list/', views.UserList.as_view(), name='users'),
    path('user/', views.UpdateUser.as_view(), name='user'),
]
