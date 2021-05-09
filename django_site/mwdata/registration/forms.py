from django import forms

from . import models


class RegistrationForm(forms.ModelForm):
    
    class Meta:
        model = models.Registration
        fields = '__all__'