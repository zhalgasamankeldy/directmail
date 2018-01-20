from django import forms

from .models import Letter


class LetterForm(forms.ModelForm):
    class Meta:
       model = Letter
       fields = '__all__' # or (‘id’, ‘file’)

