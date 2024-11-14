from django import forms

from health_assist.insurances.models import GeneralInsurance


class GInsuranceBaseForm(forms.ModelForm):
    class Meta:
        model = GeneralInsurance
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'General Insurance Title', 'class': 'form-control'}),
            'summary': forms.Textarea(attrs={'placeholder': 'Add news summary', 'class': 'form-control'}),
            'hidden_info': forms.Textarea(
                attrs={'placeholder': 'Add additional information if needed', 'class': 'form-control'}),
        }

        labels = {
            'title': 'Insurance Title',
            'hidden_info': 'Additional information',
        }


class AddGenInsuranceForm(GInsuranceBaseForm):
    pass


class EditGenInsuranceForm(GInsuranceBaseForm):
    pass


class HInsuranceBaseForm(forms.ModelForm):
    class Meta:
        model = GeneralInsurance
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Health insurance title', 'class': 'form-control'}),
            'summary': forms.Textarea(attrs={'placeholder': 'Add summary', 'class': 'form-control'}),
            'hidden_info': forms.Textarea(
                attrs={'placeholder': 'Add additional information if needed', 'class': 'form-control'}),
        }

        labels = {
            'title': 'Insurance Title',
            'hidden_info': 'Additional information',
        }


class AddHealthInsuranceForm(GInsuranceBaseForm):
    pass


class EditHealthInsuranceForm(GInsuranceBaseForm):
    pass
