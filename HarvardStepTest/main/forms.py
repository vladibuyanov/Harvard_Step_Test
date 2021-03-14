from .models import Results
from django.forms import ModelForm, TextInput


class ResultsForm(ModelForm):
    class Meta:
        model = Results
        fields = ['name', 'age', 'time', 'f1', 'f2', 'f3']
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
            ),
            'time': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Enter time"}
            ),
            'f1': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Enter f1"}
            ),
            'f2': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Enter f2"}
            ),
            'f3': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Enter f2"}
            )
        }
