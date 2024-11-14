from django.urls import path, include
#
# from health_assist.insurances import views
from health_assist.insurances.views import InsuranceListView, AddInsuranceView, EditInsuranceView

urlpatterns = [
    path('insurance/', InsuranceListView.as_view(), name='insurances'),
    path('add/', include([
        path('?type=general', AddInsuranceView.as_view(), name='add_g_insurance'),
        path('', AddInsuranceView.as_view(), name='add_h_insurance'),
    ])),
    path('<int:pk>/edit/', include([
        path('?type=general', EditInsuranceView.as_view(), name='edit_g_insurance'),
        path('health-insurance/', EditInsuranceView.as_view(), name='edit_h_insurance' ),
    ])),
    # path('<int:pk>/delete/', include([
    #     path('general-i/', DeleteGenInsurance.as_view(), name='delete-g_insurance'),
    #     path('helth-i/', DeleteHealthInsurance.as_view(), name='delete-h_insurance'),
    # ]))
]
