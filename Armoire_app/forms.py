from unicodedata import category
from attr import attrs
from django import forms
from .models import Piece


class PieceForm(forms.ModelForm):
    class Meta:
        model = Piece
        fields = ['name', 'image', 'category', 'color', 'season', 'style']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': 'required', 'autocomplete': 'off'}),
            'image': forms.FileInput(attrs={'class': 'form-control choose-file', 'required': 'required'}),
            'category': forms.Select(attrs={'class': 'form-control dropdown-content', 'required': 'required'}),
            'color': forms.Select(attrs={'class': 'form-control dropdown-content', 'required': 'required'}),
            'season': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
            'style': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),

        }
