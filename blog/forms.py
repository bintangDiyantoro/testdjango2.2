from django import forms
from .models import Artikel


class ArtikelForm(forms.ModelForm):
    class Meta:
        model = Artikel
        fields = ['judul', 'isi', 'penulis']
        widgets = {
            'judul': forms.TextInput(attrs={'placeholder': 'Judul jangan kosong'}),
            'isi': forms.Textarea(attrs={'placeholder': 'Default konsep'}),
            'penulis': forms.TextInput(attrs={'placeholder': 'Awas Jangan Otong!'}),
        }
        labels = {
            'judul':'Title'
        }
