from django.urls import path

from health_assist.common import views

urlpatterns = [
    path('', views.home_page, name='home'),
]