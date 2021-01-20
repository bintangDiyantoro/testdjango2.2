from django import forms
from .models import Artikel


class ArtikelForm(forms.ModelForm):
    class Meta:
        model = Artikel
<<<<<<< HEAD
        fields = ['judul', 'isi', 'penulis']
=======
        fields = ('judul', 'isi', 'penulis','photo')
>>>>>>> Bean
        widgets = {
            'judul': forms.TextInput(attrs={'placeholder': 'Judul jangan kosong'}),
            'isi': forms.Textarea(attrs={'placeholder': 'Default konsep'}),
            'penulis': forms.TextInput(attrs={'placeholder': 'Awas Jangan Otong!'}),
        }
        labels = {
            'judul':'Title'
<<<<<<< HEAD
        }
=======
        }
>>>>>>> Bean
