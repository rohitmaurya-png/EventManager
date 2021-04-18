from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('become-coordinator/', views.become_coordinator, name='become_coordinator'),
    path('coordinator-admin/', views.coordinator_admin, name='coordinator_admin'),
    path('add-event/', views.add_event, name='add_event'),
    path('edit-coordinator/', views.edit_coordinator, name='edit_coordinator'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='coordinator/login.html'), name='login'),
    path('', views.coordinators, name='coordinators'),
    path('<int:coordinator_id>/', views.coordinator, name='coordinator'),
]