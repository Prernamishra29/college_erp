# faculty/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.faculty_home, name='faculty_home'),  # A view for faculty home
]
