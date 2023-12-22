from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('wishlist/', views.view_wishlist, name='wishlist'),
    path('contact/', views.contact, name='contact'),
    path('submit_contact/', views.submit_contact, name='submit_contact'),
]
