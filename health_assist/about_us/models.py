from django.db import models

from mixins.models_mixins import SummaryAndHiddenInfoMixin


# Create your models here.
class AboutUs(SummaryAndHiddenInfoMixin):

    def __str__(self):
        return self.title
