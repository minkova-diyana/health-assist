from django.urls import path

from health_assist.about_us import views

urlpatterns = [
    path('about/', views.about, name='about'),
]