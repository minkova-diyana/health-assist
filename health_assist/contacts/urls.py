from django.urls import path

from health_assist.contacts import views

urlpatterns = [
    path('contacts/', views.contacts, name='contacts'),
]