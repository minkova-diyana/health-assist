from django.db import models

from mixins.models_mixins import SummaryAndHiddenInfoMixin


# Create your models here.
class News(SummaryAndHiddenInfoMixin):
    published_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title
