from django.contrib import admin

from health_assist.hnf_news.models import News


# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass