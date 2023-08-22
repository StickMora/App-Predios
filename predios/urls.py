from django.urls import path
from . import views

urlpatterns = [
    path('', views.predios_list, name='predios_list'),
    path('predio/create/', views.predio_create_edit, name='predio_create'),
    path('predio/<int:predio_id>/', views.predio_create_edit, name='predio_edit'),
    path('predio/<int:predio_id>/delete/', views.predio_delete, name='predio_delete'),
]
