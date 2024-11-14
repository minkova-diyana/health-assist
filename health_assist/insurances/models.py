from django.db import models
from django.template.defaultfilters import slugify

from mixins.models_mixins import InsuranceInfoMixin


# Create your models here.
class GeneralInsurance(InsuranceInfoMixin):

    pass


class HealthInsurance(InsuranceInfoMixin):
    pass
