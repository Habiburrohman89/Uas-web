from django.urls import path
from . import views

urlpatterns = [
    path('pengguna/', views.pengguna_list, name='pengguna_list'),
    path('pengguna/<int:pk>/', views.pengguna_detail, name='pengguna_detail'),
]
