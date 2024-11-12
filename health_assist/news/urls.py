from django.urls import path

from health_assist.news import views

urlpatterns = [
    path('news/', views.news, name='news'),
]