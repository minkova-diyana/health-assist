from django.urls import path

from health_assist.insurances import views

urlpatterns = [
    path('insurances/', views.insurances, name='insurances'),
]