#
#

from django.urls import path

#
#

from . import views

#
#
from django.contrib import admin

admin.site.site_header = "Staff Co-ordinator"
admin.site.site_title = "Welcome To Staff Co-ordinator Dashboard"
admin.site.index_title = "Welcome To Staff Co-ordinator Dashboard"

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('contact/', views.contact, name='contact')
]