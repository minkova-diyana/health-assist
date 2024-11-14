from django import forms

from health_assist.hnf_news.models import News


class NewsBaseForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'News title', 'class': 'form-control'}),
            'summary': forms.Textarea(attrs={'placeholder': 'Add news summary', 'class': 'form-control'}),
            'hidden_info': forms.Textarea(
                attrs={'placeholder': 'Add additional information', 'class': 'form-control'}),
        }

        labels = {
            'title': 'News Title',
            'hidden_info': 'Additional information',
        }


class AddNewsForm(NewsBaseForm):
    pass


class EditNewsForm(NewsBaseForm):
    pass

