from django.urls import path
from . import views

urlpatterns = [
    path('foods/', views.FoodList.as_view()),
    path('foods/<int:pk>/', views.FoodDetail.as_view()),
    path('deliveries/', views.DeliveryList.as_view()),
    path('deliveries/<int:pk>/', views.DeliveryDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('orderfoods/', views.OrderFoodList.as_view()),
    path('orderfoods/<int:pk>/', views.OrderFoodDetail.as_view()),
    path('admins/', views.AdminList.as_view()),
    path('admins/<int:pk>/', views.AdminDetail.as_view()),
    path('users/login/', views.user_login, name='user_login'),
    path('users/logout/', views.user_logout, name='user_logout'),
    path('admins/login/', views.admin_login, name='admin_login'),
    path('admins/logout/', views.admin_logout, name='admin_logout'),
]