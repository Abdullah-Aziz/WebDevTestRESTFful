from django.urls import path
from . import views


urlpatterns = [
    path('', views.api_overview, name='api_overview'),
    path('product_list/', views.product_list, name='product_list'),
    path('product_create/', views.product_create, name='product_create'),
    path('product_sold/', views.product_sold, name='product_sold'),
    path('product_remaining/', views.product_remaining, name='product_remaining'),
    path('product_update/<str:pk>/', views.product_update, name='product_update'),
    path('product_retrieve/<str:pk>/', views.product_retrieve, name='product_retrieve'),
 ]
