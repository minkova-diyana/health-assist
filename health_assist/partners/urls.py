from django.urls import path

from health_assist.partners import views

urlpatterns = [
    path('partners/', views.partners, name='partners'),
]
