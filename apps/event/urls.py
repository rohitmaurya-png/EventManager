from django.urls import path

from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('<slug:category_slug>/<slug:event_slug>/', views.event, name='event'),
    path('<slug:category_slug>/', views.category, name='category')
]