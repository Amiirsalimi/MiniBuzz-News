from django import forms
from .models import NewsEntry

class NewsEntryForm(forms.ModelForm):
    class Meta:
        model = NewsEntry
        fields = ['title', 'summary']
