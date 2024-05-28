from django import forms
from .models import Section, Word


class FormSection(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['name']


class FormWord(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['foreign_word', 'native_word']
