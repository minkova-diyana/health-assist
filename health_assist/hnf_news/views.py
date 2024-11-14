from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from health_assist.hnf_news.forms import AddNewsForm, EditNewsForm
from health_assist.hnf_news.models import News


# Create your views here.
def hnf_news(request):
    news = News.objects.all()

    context = {'news': news}
    return render(request, 'news/news.html', context)


class AddNewsView(CreateView):
    model = News
    form_class = AddNewsForm
    template_name = 'news/add-news.html'
    success_url = reverse_lazy('news')
    context_object_name = 'news'


class EditNewsView(UpdateView):
    model = News
    form_class = EditNewsForm
    template_name = 'news/edit-news.html'
    success_url = reverse_lazy('news')
    context_object_name = 'news'


def delete_news(request, pk):
    news = News.objects.get(pk=pk)
    news.delete()
    return redirect(request.META.get('HTTP_REFERER'))
