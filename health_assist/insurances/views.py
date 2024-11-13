from django.views.generic import ListView

from health_assist.insurances.models import GeneralInsurance, HealthInsurance


class InsuranceListView(ListView):
    model = GeneralInsurance
    template_name = 'insurances/insurances.html'
    context_object_name = 'general_insurances'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['health_insurance'] = HealthInsurance.objects.all()

        return context
