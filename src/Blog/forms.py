from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'date',
            'abstract',
            'body'
        ]

    def clean_title(self):
        title = self.cleaned_data.geta('title')
        if title.lower() == 'abc':
            raise forms.ValidationError("This is not a valid title")
        return title