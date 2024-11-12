from django.db import models


class SummaryAndHiddenInfoMixin(models.Model):
    title = models.CharField(max_length=50)
    summary = models.TextField(max_length=200)
    hidden_info = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True
