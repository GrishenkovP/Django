from django import forms
from .models import Step

class StepForm(forms.ModelForm):
    class Meta:
        model = Step
        fields = '__all__'


