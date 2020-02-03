from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class meta:
        model = Article
        field = [
            'title',
            'date',
            'abstract',
            'body'
        ]