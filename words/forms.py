# yourappname/forms.py

from django import forms
from .models import Word, Theme

class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['original_word', 'translated_word', 'transcription']


class ThemeForm(forms.ModelForm):
    class Meta:
        model = Theme
        fields = ['name', 'date']