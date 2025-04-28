from django.urls import path
from django.conf import settings
from . import views

# Base URL patterns
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact_form, name='contact_form'),  
    path('success/', views.contact_success, name='contact_success'),
    path('projects/', views.project_list, name='project_list'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
]
