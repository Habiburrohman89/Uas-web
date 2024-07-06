from django.urls import path
from . import views

urlpatterns = [
    path('kategori/', views.kategori_list, name='kategori-list'),
    path('kategori/<int:pk>/', views.kategori_detail, name='kategori-detail'),
]
