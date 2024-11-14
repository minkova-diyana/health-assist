from django.db import models
from django.template.defaultfilters import slugify


class SummaryAndHiddenInfoMixin(models.Model):
    SUMMARY_MAX_LENGTH = 200
    title = models.CharField(max_length=50)
    summary = models.TextField(max_length=SUMMARY_MAX_LENGTH)
    hidden_info = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True


class InsuranceInfoMixin(SummaryAndHiddenInfoMixin):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    slug = models.SlugField(
        null=True,
        blank=True,
        unique=True,
        editable=False,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True

