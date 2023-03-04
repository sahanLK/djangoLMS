from django import forms
from .models import Classroom


class ClassCreationForm(forms.ModelForm):
    class Meta:
        model = Classroom
        fields = ['name', 'subtitle_1', 'subtitle_2', 'description']
