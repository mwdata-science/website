from django import forms

from . import models


class RegistrationForm(forms.ModelForm):
    date_of_bith = forms.DateField(
        widget=forms.SelectDateWidget(attrs={"class": "dob"})
    )

    class Meta:
        model = models.Registration
        fields = "__all__"
