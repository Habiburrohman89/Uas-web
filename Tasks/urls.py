from django.urls import path
from . import views

urlpatterns = [
    path('tugas/', views.tugas_list, name='tugas_list'),
    path('tugas/<int:pk>/', views.tugas_detail, name='tugas_detail'),
]
