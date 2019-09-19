from django import forms
from .models import Observations

class ObsForm(forms.ModelForm):
    class Meta:
        model = Observations
        fields = ['description_text',]