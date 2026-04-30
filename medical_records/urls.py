from django.urls import path
from . import views

urlpatterns = [
    # Doctors
    path('doctors/', views.doctor_list_view, name='doctor_list'),
    path('doctors/add/', views.doctor_form_view, name='doctor_add'),
    path('doctors/<int:doctor_id>/', views.doctor_detail_view, name='doctor_detail'),
    path('doctors/<int:doctor_id>/delete/', views.doctor_delete_view, name='doctor_delete'),

    # Services
    path('services/', views.service_list_view, name='service_list'),
    path('services/add/', views.service_form_view, name='service_add'),
    path('services/<int:service_id>/', views.service_detail_view, name='service_detail'),
    path('services/<int:service_id>/delete/', views.service_delete_view, name='service_delete'),

    # Categories
    path('categories/', views.category_list_view, name='category_list'),
    path('categories/add/', views.category_form_view, name='category_add'),
    # ... і так далі для деталей та видалення категорій
]