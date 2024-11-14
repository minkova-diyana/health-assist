from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, ListView

from health_assist.about_us.forms import EditAboutForm
from health_assist.about_us.models import AboutUs


# Create your views here.
class AboutUsDetailView(ListView):
    model = AboutUs
    template_name = 'about_us/about-us.html'
    context_object_name = 'about_us'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about_us'] = AboutUs.objects.first()
        return context


class EditAboutUsView(UpdateView):
    model = AboutUs
    form_class = EditAboutForm
    success_url = reverse_lazy('about')
    template_name = 'about_us/edit-about-us.html'
    context_object_name = 'about_us'
