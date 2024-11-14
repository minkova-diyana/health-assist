from django.urls import path, include

from health_assist.hnf_news import views
from health_assist.hnf_news.views import AddNewsView, EditNewsView, delete_news

urlpatterns = [
    path('news/', views.hnf_news, name='news'),
    path('add-news/', AddNewsView.as_view(), name='add-news'),
    path('<int:pk>/', include([
        path('edit-news/', EditNewsView.as_view(), name='edit_news'),
        path('delete-news/', delete_news, name='delete-news'),
    ]))
]