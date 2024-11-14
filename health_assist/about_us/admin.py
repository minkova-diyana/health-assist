from django.contrib import admin

from health_assist.about_us.models import AboutUs


# Register your models here.
@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    pass