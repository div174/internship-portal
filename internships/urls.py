from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Public routes
    path('', views.index, name='index'),
    path('apply/', views.apply, name='apply'),
    
    # Auth routes
    path('dashboard/login/', views.admin_login, name='login'),
    path('dashboard/logout/', views.admin_logout, name='logout'),
    
    # Dashboard routes
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/applicants/', views.applicants_list, name='applicants'),
    path('dashboard/applicants/<int:pk>/', views.applicant_detail, name='applicant_detail'),
    path('dashboard/applicants/<int:pk>/status/<str:status>/', views.update_status, name='update_status'),
    path('dashboard/applicants/<int:pk>/delete/', views.delete_applicant, name='delete_applicant'),
    path('dashboard/settings/', views.dashboard_settings, name='settings'),
]
