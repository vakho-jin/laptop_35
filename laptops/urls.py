from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('store/<int:pk>/', views.store_profile, name='store_profile'),
    path('laptop/<int:pk>/', views.laptop_detail, name='laptop_detail'),
    path('laptop/create/', views.LaptopCreateView.as_view(), name='laptop_create'),
    path('laptop/<int:pk>/update/', views.LaptopUpdateView.as_view(), name='laptop_update'),
    path('laptop/<int:pk>/delete/', views.LaptopDeleteView.as_view(), name='laptop_delete'),
    path('search/', views.search_laptops, name='search_laptops'),
]