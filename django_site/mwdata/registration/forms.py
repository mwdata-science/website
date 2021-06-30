from django import forms

from . import models


BIRTH_YEAR_CHOICES = range(1900, 2010)


class RegistrationForm(forms.ModelForm):
    date_of_bith = forms.DateField(
        widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES, attrs={"class": "dob"})
    )

    def clean(self):
        raise forms.ValidationError("Registration is closed :/")

    class Meta:
        model = models.Registration
        fields = "__all__"
