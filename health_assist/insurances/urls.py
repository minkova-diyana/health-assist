from django.urls import path, include
#
# from health_assist.insurances import views
from health_assist.insurances.views import InsuranceListView

urlpatterns = [
    path('insurance/', InsuranceListView.as_view(), name='insurances')
]