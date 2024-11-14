from django.urls import path

from health_assist.about_us import views
from health_assist.about_us.views import AboutUsDetailView, EditAboutUsView

urlpatterns = [
    path('about/', AboutUsDetailView.as_view(), name='about'),
    path('<int:pk>/edit-about-us/', EditAboutUsView.as_view(), name='edit_about'),
]