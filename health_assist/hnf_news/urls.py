from django.urls import path

from health_assist.hnf_news import views

urlpatterns = [
    path('news/', views.hnf_news, name='news'),
]