from django import forms
from .models import Article


class submitArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'Title',
            'Author',
            'Publication_date',
            'Journal',
            'Volume',
            'Issue',
            'Article_Description',
            'User_ID'      
        ]