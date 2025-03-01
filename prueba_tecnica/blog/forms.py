from django import forms
from .models import BlogEntry

class BlogEntryForm(forms.ModelForm):
    class Meta:
        model = BlogEntry
        fields = ['title', 'content']
        labels = {
            'title': 'Título',
            'content': 'Contenido',
        }