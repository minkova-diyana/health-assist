from django.db import models

from mixins.mixins import SummaryAndHiddenInfoMixin


# Create your models here.
class Insurance(SummaryAndHiddenInfoMixin):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



