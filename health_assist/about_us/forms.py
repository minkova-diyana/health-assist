from django import forms

from health_assist.about_us.models import AboutUs


class AboutBaseForm(forms.ModelForm):
    class Meta:
        model = AboutUs
        fields = '__all__'

        labels = {
            'title': 'HealthNet Moto',
            'hidden_info': 'Additional information',
        }

        error_messages = {
            'title': {
                'required': 'Title cannot be empty',
            },
            'summary': {
                'required': 'Summary cannot be empty',
                'max_length': f'Summary cannot be more than {AboutUs.SUMMARY_MAX_LENGTH} characters',
            }
        }


class EditAboutForm(AboutBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['summary'].widget.attrs.update({
            'class': 'form-control',

        })

        self.fields['hidden_info'].widget.attrs.update({
            'class': 'form-control',
        })
