from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from health_assist.insurances.forms import AddHealthInsuranceForm, AddGenInsuranceForm, EditGenInsuranceForm, \
    EditHealthInsuranceForm
from health_assist.insurances.models import GeneralInsurance, HealthInsurance


class InsuranceListView(ListView):
    model = GeneralInsurance
    template_name = 'insurances/insurances.html'
    context_object_name = 'general_insurances'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['health_insurance'] = HealthInsurance.objects.all()

        return context


class AddInsuranceView(CreateView):

    template_name = 'insurances/add-insurance.html'
    success_url = reverse_lazy('insurances')
    context_object_name = 'insurance'

    def get_model(self):
        if self.request.GET.get('type') == 'general':
            return GeneralInsurance
        return HealthInsurance

    def get_form_class(self):
        if self.request.GET.get('type') == 'general':
            return AddGenInsuranceForm
        return AddHealthInsuranceForm


class EditInsuranceView(UpdateView):
    template_name = 'insurances/edit-insurance.html'
    success_url = reverse_lazy('insurances')
    context_object_name = 'insurance'

    def get_model(self):
        if self.request.GET.get('type') == 'general':
            return GeneralInsurance
        return HealthInsurance

    def get_form_class(self):
        if self.request.GET.get('type') == 'general':
            return EditGenInsuranceForm
        return EditHealthInsuranceForm

