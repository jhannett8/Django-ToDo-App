from django import forms 
from .models import Task_model


class Task_form(forms.ModelForm):
    class Meta: 
        model = Task_model
        fields = [
            'timeframe',
            'title', 
            'date', 
            'description',
            'completed',
        ]



