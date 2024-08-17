from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),  # Home page URL
    path('register/', views.register, name='register'),  # Registration page URL
]
