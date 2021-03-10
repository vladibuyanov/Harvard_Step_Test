from .models import Results
from django.forms import ModelForm, TextInput


class ResultsForm(ModelForm):
    class Meta:
        model = Results
        fields = ['name', 'age']
        widgets = {
            'name': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Enter your name"}
            ),
            'age': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Enter your age"}
            )
        }
