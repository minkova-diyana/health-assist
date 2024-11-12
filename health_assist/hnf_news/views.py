from django.shortcuts import render

from health_assist.hnf_news.models import News


# Create your views here.
def hnf_news(request):
    news = News.objects.all()

    context = {'news': news}
    return render(request, 'news/news.html', context)
