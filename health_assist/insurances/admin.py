from django.contrib import admin

from health_assist.insurances.models import GeneralInsurance, HealthInsurance


# Register your models here.
@admin.register(GeneralInsurance)
class GeneralInsuranceAdmin(admin.ModelAdmin):
    pass


@admin.register(HealthInsurance)
class HealthInsuranceAdmin(admin.ModelAdmin):
    pass
